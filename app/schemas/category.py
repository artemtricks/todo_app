from pydantic import BaseModel


class CategorySchema(BaseModel):
    model_config = {"from_attributes": True}

    id: str
    name: str

class CategoryCreateSchema(BaseModel):
    name: str