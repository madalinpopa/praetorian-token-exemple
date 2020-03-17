# coding: utf-8


# tests/conftest.py

import pytest
from sqlalchemy.orm import clear_mappers, scoped_session, sessionmaker
from sqlalchemy import create_engine

from app import guard
from app import create_app

from app.orm import metadata, start_mapper


@pytest.fixture
def engine():
    engine = create_engine("sqlite:///test.db", echo=True)
    metadata.create_all(bind=engine)
    yield engine


@pytest.fixture
def session(engine):
    session = scoped_session(sessionmaker(bind=engine))


@pytest.fixture
def app_instance(engine, session):
    app_test = create_app()
    start_mapper()
    yield app_test


@pytest.fixture
def client(app_instance):

    with app_instance.test_client() as client:
        yield client
