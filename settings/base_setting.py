from pydantic import BaseSettings


class Settings(BaseSettings):
    DB_HOST: str = "localhost"
    DB_PORT: str = "3306"
    DB_USER: str = "sw"
    DB_PASS: str = "22380476"
    DB_DATABASE = "ci_project_db"
