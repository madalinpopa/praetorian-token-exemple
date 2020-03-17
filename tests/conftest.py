# coding: utf-8


# tests/conftest.py

import pytest
from sqlalchemy.orm import clear_mappers
from sqlalchemy import create_engine

from app import guard

from app import create_app
from app.database import Session
from app.model import User
from app.orm import metadata, start_mapper


@pytest.fixture
def client():

    engine = create_engine("sqlite:///test.db")

    application = create_app()

    with application.test_client() as client:
        with application.app_context():
            start_mapper()
            metadata.create_all(bind=engine)
            init_users()
        yield client

    clear_mappers()
    Session.remove()


def init_users():

    user1 = User("user1", guard.hash_password("secret1"))
    user2 = User("user2", guard.hash_password("secret2"))
    user3 = User("user3", guard.hash_password("secret3"))
    Session.add_all([user1, user2, user3])
    Session.commit()
