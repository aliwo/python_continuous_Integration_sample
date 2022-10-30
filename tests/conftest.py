import asyncio
from asyncio import AbstractEventLoop
from typing import Any, Generator
from unittest.mock import Mock, patch

import pytest
from pytest import FixtureRequest
from tortoise import generate_config
from tortoise.contrib.test import finalizer, initializer

from database.config import TORTOISE_APP_MODELS
from settings import settings

TEST_BASE_URL = "http://test"
TEST_DB_LABEL = "models"
TEST_DB_TZ = "Asia/Seoul"


def get_test_db_config() -> Any:
    config = generate_config(
        db_url=f"mysql://{settings.DB_USER}:{settings.DB_PASS}@{settings.DB_HOST}:{settings.DB_PORT}/{settings.DB_DATABASE}",
        app_modules={TEST_DB_LABEL: TORTOISE_APP_MODELS},
        connection_label=TEST_DB_LABEL,
        testing=True,
    )
    config["timezone"] = TEST_DB_TZ

    return config


@pytest.fixture(scope="session")
def event_loop() -> Generator[AbstractEventLoop, None, None]:
    loop = asyncio.get_event_loop()
    yield loop
    loop.close()


@pytest.fixture(scope="session", autouse=True)
def initialize(request: FixtureRequest) -> None:
    with patch("tortoise.contrib.test.getDBConfig", Mock(return_value=get_test_db_config())):
        initializer(modules=TORTOISE_APP_MODELS)
    request.addfinalizer(finalizer)
