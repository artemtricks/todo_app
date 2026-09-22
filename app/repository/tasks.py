from sqlalchemy.orm import Session, joinedload
from app.schemas.task import TaskSchema, TaskWithCategorySchema
from app.models.tasks import TaskORM




class TaskRepository:
    def __init__(self, db: Session) -> None:
        self.db = db

    def get_all(self) -> list[TaskWithCategorySchema]:
        return self.db.query(TaskORM).options(joinedload(TaskORM.categories)).all()

    def create(self, title: str, category_id: str) -> TaskSchema:
        new_task = TaskORM(title=title, completed=False, category_id=category_id)  
        self.db.add(new_task)
        return new_task
        
    def get_by_id(self, task_id: str) -> TaskSchema:
        return self.db.get(TaskORM, task_id)

    def delete(self, TaskOrm: TaskORM) -> None:
        self.db.delete(TaskOrm)
