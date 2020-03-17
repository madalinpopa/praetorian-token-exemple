# coding: utf-8

# app/database.py

from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import scoped_session, sessionmaker

import config

engine = create_engine(config.Config().SQLALCHEMY_DATABASE_URI)
metadata = MetaData()
db_session = scoped_session(
    sessionmaker(bind=engine, autocommit=False, autoflash=False,)
)


def init_prod_db():
    metadata.create_all(bind=engine)

def init_test_db():
    metadata.create_all(bind=engine)