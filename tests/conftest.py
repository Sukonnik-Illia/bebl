import pytest
from freezegun import freeze_time
from bebl.main import create_app
from bebl.db import db


@pytest.fixture
def app():
    yield create_app()


@pytest.fixture
def client(app):
    yield app.test_client()
    db.clear_db()


@pytest.fixture
def frozen_time():
    with freeze_time("2024-03-30") as frozen_time:
        yield frozen_time
