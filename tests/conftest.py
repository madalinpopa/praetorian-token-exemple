# coding: utf-8


# tests/conftest.py

import pytest

from app import create_app

from app.database import engine, Session
from app.orm import metadata, start_mapper

@pytest.fixture
def client():
    application = create_app()
    application.testing = True
    application.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///:memory:"
    client = application.test_client()

    with application.app_context():
        start_mapper()
        metadata.create_all(bind=engine)
    application.app_context().push()

    yield client
    Session.remove()