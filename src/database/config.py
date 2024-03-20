from pydantic_settings import BaseSettings


class Setting(BaseSettings):
    db_url: str = f"postgresql+asyncpg://postgres:hleb@localhost:5432/postgres"
    db_echo: bool = True


settings = Setting()
