from fastapi import APIRouter, Depends, status
from app.schemas.task import TaskCreateSchema, TaskSchema, TaskUpdateSchema, TaskWithCategorySchema
from app.service.tasks import TaskService
from app.api.dependencies import get_task_service

router = APIRouter()



@router.get('/tasks')
def get_tasks(task_service: TaskService = Depends(get_task_service)) -> list[TaskWithCategorySchema]:
     return task_service.list_tasks()
 


@router.post('/tasks')
def create_tasks(payload: TaskCreateSchema, task_service: TaskService = Depends(get_task_service)) -> TaskSchema:
    return task_service.create_task(payload.title, payload.category_id)


@router.patch('/tasks/{task_id}')
def update_task(task_id: str, payload: TaskUpdateSchema, task_service: TaskService = Depends(get_task_service)) -> TaskSchema:
    return task_service.update_task(task_id=task_id, task_update=payload)
            


@router.delete('/tasks/{task_id}', status_code=status.HTTP_204_NO_CONTENT)
def delete_task(task_id:str, task_service: TaskService = Depends(get_task_service)):
    return task_service.delete_task(task_id=task_id)
    
    