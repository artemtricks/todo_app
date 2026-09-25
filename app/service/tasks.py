from fastapi import HTTPException

from app.repository.tasks import TaskRepository
from sqlalchemy.orm import Session
from app.schemas.task import TaskSchema, TaskUpdateSchema, TaskWithCategorySchema
from app.repository.category import CategoryRepository
from app.cache.redis import RedisCacheBackend
from app.core.config import get_setting



settings = get_setting()
class TaskService:
    def __init__(self, db: Session) -> None:
        self.db = db
        self.task_repository = TaskRepository(db)
        self.category_repository = CategoryRepository(db)
        self.cache = RedisCacheBackend(redis_url=settings.redis_url, cache_ttl_seconds=settings.cache_ttl_seconds)
        
    def list_tasks(self) -> list[TaskWithCategorySchema]:
        # 1. Проверить есть ли данные в Redis 
        cached_tasks = self.cache.get(settings.cache_tasks_key)

        if cached_tasks is not None:
            return cached_tasks
        
        # 2. идем в БД если данных в кэше нет
        tasks_orm = self.task_repository.get_all() 

        # 3. записываем данные в кэш
        tasks_read = [TaskWithCategorySchema.model_validate(task) for task in tasks_orm]
        tasks_for_cache = [task.model_dump() for task in tasks_read]
        self.cache.set(settings.cache_tasks_key, tasks_for_cache)

        return tasks_read

    def create_task(self, title: str, category_id: str) -> TaskSchema:
        # инвалидация кэша
        self.cache.delete(settings.cache_tasks_key)


        category = self.category_repository.get_by_id(category_id=category_id)
        if not category:
             raise HTTPException(404,  f'Category with {category_id} not found')

        new_task_orm = self.task_repository.create(title=title, category_id=category_id)
        self.db.commit()
        return TaskSchema.model_validate(new_task_orm)

    def delete_task(self, task_id: str) -> None:
         # инвалидация кэша
        self.cache.delete(settings.cache_tasks_key)


        delete_task = self.task_repository.get_by_id(task_id)
        if not delete_task:
            raise HTTPException(404, f'Task id {task_id} not found')
        self.db.commit()
        return self.task_repository.delete(delete_task)

    def update_task(self, task_id: str, task_update: TaskUpdateSchema) -> TaskSchema: 
         # инвалидация кэша
        self.cache.delete(settings.cache_tasks_key)


        task_for_update = self.task_repository.get_by_id(task_id)

        if not task_for_update:
                 raise HTTPException(404, f'Task id {task_id} not found')
        
        if task_update.title is not None:
            task_for_update.title = task_update.title
        if task_update.completed is not None:
            task_for_update.completed = task_update.completed
        self.db.commit()
        return TaskSchema.model_validate(task_for_update)
       