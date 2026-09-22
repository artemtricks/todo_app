
from app.repository.category import CategoryRepository
from sqlalchemy.orm import Session
from app.schemas.category import CategorySchema

class CategoryService():
    def __init__(self, db: Session) -> None:
        self.db = db
        self.category_repository = CategoryRepository(db)

    def get_all(self) -> list[CategorySchema]:
        categories_orm = self.category_repository.get_all()
        return [CategorySchema.model_validate(category) for category in categories_orm]

    def create(self, name: str) -> CategorySchema:
        new_category = self.category_repository.create(name=name)
        self.db.commit()
        return CategorySchema.model_validate(new_category)

    