from dataclasses import dataclass



@dataclass(frozen=True)
class Settings:
    DATABASE_URL: str
    allow_origins_url: list[str]




def get_setting():
    return Settings(
            DATABASE_URL = "postgresql+psycopg://postgres:postgres@localhost:5432/todo",
            allow_origins_url = ["http://localhost:3000"]
        )




