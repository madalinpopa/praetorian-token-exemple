# coding: utf-8

# app/database.py

from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import scoped_session, sessionmaker

import config

engine = create_engine(config.Config().SQLALCHEMY_DATABASE_URI)
test_engine = create_engine("sqlite:///test.db")
metadata = MetaData()
db_session = scoped_session(
    sessionmaker(bind=engine, autocommit=False, autoflush=False,)
)

test_session = scoped_session(
    sessionmaker(bind=test_engine, autocommit=False, autoflush=False)
)


def init_prod_db():
    metadata.create_all(bind=engine)


def init_test_db():
    metadata.create_all(bind=test_engine)
