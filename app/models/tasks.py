from sqlalchemy import ForeignKey
from sqlalchemy.orm import  Mapped,  mapped_column, relationship
from app.models.base import Base
from app.models.category import CategoryORM


class TaskORM(Base):
    __tablename__ = 'tasks'

    title: Mapped[str]
    completed: Mapped[bool] = mapped_column(default=False)
    category_id: Mapped[str] = mapped_column(ForeignKey('categories.id'))
    categories: Mapped["CategoryORM"] = relationship()


    

