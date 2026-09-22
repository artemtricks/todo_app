from sqlalchemy.orm import Session
from app.models.category import CategoryORM
from app.schemas.category import CategorySchema






class CategoryRepository:
    def __init__(self, db: Session) -> None:
        self.db = db
      
    def get_all(self) -> list[CategorySchema]:
        return self.db.query(CategoryORM).all()

    def create(self, name: str) -> CategorySchema:
        new_category = CategoryORM(name=name)
        self.db.add(new_category)
        return new_category

    def get_by_id(self, category_id: str) -> CategorySchema | None:
            return self.db.query(CategoryORM).filter(CategoryORM.id == category_id).first()
            