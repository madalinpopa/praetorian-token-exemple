# coding: utf-8

# wsgi.py

from app import create_app
from app.orm import start_mapper
from manage import create_users, user
from database import db_session

app = create_app()

app.cli.add_command(create_users)
app.cli.add_command(user)


@app.before_first_request
def start_model_mapper():
    start_mapper()


@app.teardown_appcontext
def cleanup(resp_or_exception):
    db_session.remove()


if __name__ == "__main__":
    app.run()
