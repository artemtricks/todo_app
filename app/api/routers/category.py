from fastapi import APIRouter, Depends, status
from app.service.category import CategoryService
from app.api.dependencies import get_category_service
from app.schemas.category import CategoryCreateSchema, CategorySchema



router = APIRouter()


@router.get('/categories')
def get_categories(category_service: CategoryService = Depends(get_category_service)) -> list[CategorySchema]:
    return category_service.get_all()


@router.post('/categories', status_code=status.HTTP_201_CREATED)
def create_category(name: str, category_service: CategoryService = Depends(get_category_service)) -> CategorySchema:
    return category_service.create(name=name)
