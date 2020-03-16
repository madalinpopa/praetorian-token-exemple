# coding: utf-8

# app/database.py

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

import config

engine = create_engine(config.Config().SQLALCHEMY_DATABASE_URI)

Session = scoped_session(sessionmaker(bind=engine))
