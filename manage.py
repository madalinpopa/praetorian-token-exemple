# coding: utf-8

# manage.py

import click
from flask.cli import with_appcontext

from app import guard
from app.model import User

from app.database import db_session, init_prod_db, init_test_db
from app.orm import start_mapper, metadata


@click.command(name="init")
@with_appcontext
def init():
    start_mapper()
    init_prod_db()

    user1 = User("user1", guard.hash_password("secret1"))
    user2 = User(username="user2", password=guard.hash_password("secret2"))
    user3 = User(username="user3", password=guard.hash_password("secret3"))

    Session.add_all([user1, user2, user3])
    Session.commit()


@click.command(name="user")
@with_appcontext
def user():
    start_mapper()
    user = guard.authenticate("user1", "secret1")
    print(user)
