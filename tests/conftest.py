# coding: utf-8


# tests/conftest.py

import pytest

from app import guard
from app import create_app

from app.database import init_test_db
from app.orm import start_mapper

@pytest.fixture
def app_instance():
    app_test = create_app()

    yield app_test


@pytest.fixture
def client(app_instance):

    with app_instance.test_client() as client:
        yield client
