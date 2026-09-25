from dataclasses import dataclass



@dataclass(frozen=True)
class Settings:
    DATABASE_URL: str
    allow_origins_url: list[str]
    redis_url: str
    cache_ttl_seconds: int
    cache_tasks_key: str




def get_setting():
    return Settings(
            DATABASE_URL = "postgresql+psycopg://postgres:postgres@localhost:5432/todo",
            allow_origins_url = ["http://localhost:3000"],
            redis_url="redis://localhost:6379/0",
            cache_ttl_seconds=3600,
            cache_tasks_key="cache:tasks_list"
        )




