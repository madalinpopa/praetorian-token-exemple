# coding: utf-8

# app/orm.py

from sqlalchemy import Column, ForeignKey, Integer, MetaData, String, Table
from sqlalchemy.orm import mapper, relationship

from app.model import User
from app.database import metadata


user = Table(
    "user",
    metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("username", String(50), nullable=False),
    Column("password", String(250), nullable=False),
    Column("roles", String(30), nullable=True),
)


def start_mapper():
    mapper(User, user)
