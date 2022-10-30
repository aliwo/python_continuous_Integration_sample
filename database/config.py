from settings import settings

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
                "host": settings.DB_HOST,
                "port": settings.DB_PORT,
                "user": settings.DB_USER,
                "password": settings.DB_PASS,
                "database": settings.DB_DATABASE,
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
