from sqlalchemy.orm import  declarative_base, sessionmaker
from sqlalchemy import create_engine
from app.core.config import get_setting


settings = get_setting()
engine = create_engine(settings.DATABASE_URL)

SessionLocal = sessionmaker(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally: db.close()