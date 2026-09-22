from app.db.session import get_db
from sqlalchemy.orm import Session
from fastapi import Depends
from app.service.tasks import TaskService
from app.service.category import CategoryService


def get_task_service(db:Session = Depends(get_db)):
    """Функция для инъекции зависимости TaskService"""
    return TaskService(db)


def get_category_service(db:Session = Depends(get_db)):
    """Функция для инъекции зависимости CategoryService"""
    return CategoryService(db)