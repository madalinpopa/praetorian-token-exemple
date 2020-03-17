# coding: utf-8

# wsgi.py

from app import create_app
from app.orm import start_mapper
from database import db_session
from manage import init

app = create_app()

app.cli.add_command(init)


@app.before_first_request
def start_model_mapper():
    start_mapper()


@app.teardown_appcontext
def cleanup(resp_or_exception):
    db_session.remove()


if __name__ == "__main__":
    app.run()
