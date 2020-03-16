# coding: utf-8

# app/__init__.py

from flask import Flask
from flask_praetorian import Praetorian

from app.model import User

guard = Praetorian()


def create_app():
    app = Flask(__name__)
    app.config.from_object("config.Config")

    guard.init_app(app, User)

    from app.routes import api

    app.register_blueprint(api)

    return app
