from fastapi import FastAPI
from tortoise import Tortoise
from tortoise.contrib.fastapi import register_tortoise

DB_MASTER_ALIAS = "default"


TORTOISE_APP_MODELS = [
    "database.memo",
    "aerich.models",
]

TORTOISE_ORM = {
    "connections": {
        DB_MASTER_ALIAS: {
            "engine": "tortoise.backends.mysql",
            "credentials": {
                "host": "localhost",
                "port": "3306",
                "user": "sw",
                "password": "22380476",
                "database": "ci_project_db",
                "connect_timeout": 5,
            },
        },
    },
    "apps": {
        "models": {
            "models": TORTOISE_APP_MODELS,
        },
    },
    "timezone": "Asia/Seoul",
}


# def initialize(app: FastAPI) -> None:
#     Tortoise.init_models(TORTOISE_APP_MODELS, "models")
#     register_tortoise(app, config=TORTOISE_ORM)
