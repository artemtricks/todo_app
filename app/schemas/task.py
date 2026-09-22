from pydantic import BaseModel

from app.schemas.category import CategorySchema


class TaskSchema(BaseModel):
    model_config = {"from_attributes": True}

    id: str
    title: str
    completed: bool
    category_id: str


class TaskWithCategorySchema(BaseModel):
    model_config = {"from_attributes": True}

    id: str
    title: str
    completed: bool
    categories: CategorySchema

class TaskCreateSchema(BaseModel):
    title: str
    category_id: str
   
class TaskUpdateSchema(BaseModel):
    title: str | None = None
    completed: bool | None = None


