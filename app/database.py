# coding: utf-8

# app/database.py

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

engine = create_engine("sqlite:///api.db")

Session = scoped_session(sessionmaker(bind=engine))
