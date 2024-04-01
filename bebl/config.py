from pydantic import PostgresDsn, validator
from pydantic_settings import BaseSettings


class Config(BaseSettings):
    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
        extra = "ignore"

    POSTGRES_USER: str
    POSTGRES_DB: str
    POSTGRES_PASSWORD: str
    POSTGRES_HOST: str

    SQLALCHEMY_DATABASE_URI: Optional[str] = None

    @validator("SQLALCHEMY_DATABASE_URI", pre=True)
    @classmethod
    def assemble_db_connection(cls, v: Optional[str], values: Dict[str, Any]) -> Any:
        if isinstance(v, str):
            return v
        return PostgresDsn.build(
            scheme="postgresql",
            username=values.get("POSTGRES_USER"),
            password=values.get("POSTGRES_PASSWORD"),
            host=values.get("POSTGRES_HOST"),
            path=f"/{values.get('POSTGRES_DB') or ''}",
        ).unicode_string()
