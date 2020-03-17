# coding: utf-8

# manage.py

import click
from flask.cli import with_appcontext

from app import guard
from app.model import User

from app.database import db_session, init_prod_db, init_test_db, db_test_session
from app.orm import start_mapper, metadata


@click.command(name="init_prod")
@with_appcontext
def init_prod():
    start_mapper()
    init_prod_db()

    user1 = User("user1", guard.hash_password("secret1"))
    user2 = User(username="user2", password=guard.hash_password("secret2"))
    user3 = User(username="user3", password=guard.hash_password("secret3"))

    db_session.add_all([user1, user2, user3])
    db_session.commit()


@click.command(name="init_test")
@with_appcontext
def init_test():
    start_mapper()
    init_test_db()

    user1 = User(username="user1", password=guard.hash_password("secret1"))
    db_test_session.add(user1)
    db_test_session.commit()


@click.command(name="testdb")
@with_appcontext
def testdb():
    start_mapper()
    user = User.query.get(1)
    print(user)
