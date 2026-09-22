from fastapi import HTTPException

from app.repository.tasks import TaskRepository
from sqlalchemy.orm import Session
from app.schemas.task import TaskSchema, TaskUpdateSchema, TaskWithCategorySchema
from app.repository.category import CategoryRepository

class TaskService:
    def __init__(self, db: Session) -> None:
        self.db = db
        self.task_repository = TaskRepository(db)
        self.category_repository = CategoryRepository(db)

    def list_tasks(self) -> list[TaskWithCategorySchema]: 
        tasks_orm = self.task_repository.get_all()
        print
        return [TaskWithCategorySchema.model_validate(task) for task in tasks_orm]

    def create_task(self, title: str, category_id: str) -> TaskSchema:
        category = self.category_repository.get_by_id(category_id=category_id)
        if not category:
             raise HTTPException(404,  f'Category with {category_id} not found')

        new_task_orm = self.task_repository.create(title=title, category_id=category_id)
        self.db.commit()
        return TaskSchema.model_validate(new_task_orm)

    def delete_task(self, task_id: str) -> None:
        delete_task = self.task_repository.get_by_id(task_id)
        if not delete_task:
            raise HTTPException(404, f'Task id {task_id} not found')
        return self.task_repository.delete(delete_task)

    def update_task(self, task_id: str, task_update: TaskUpdateSchema) -> TaskSchema: 

        task_for_update = self.task_repository.get_by_id(task_id)

        if not task_for_update:
                 raise HTTPException(404, f'Task id {task_id} not found')
        
        if task_update.title:
            task_for_update.title = task_update.title
        if task_update.completed is not None:
            task_for_update.completed = task_update.completed
        self.db.commit()
        return TaskSchema.model_validate(task_for_update)
       