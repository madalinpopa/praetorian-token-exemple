# coding: utf-8

# wsgi.py

from sqlalchemy.orm import clear_mappers
from app import create_app
from app.database import Session
from app.orm import start_mapper
from manage import create_users, user

app = create_app()

app.cli.add_command(create_users)
app.cli.add_command(user)

@app.before_request
def mapper():
    start_mapper()


@app.teardown_appcontext
def cleanup(resp_or_exception):
    Session.remove()
    clear_mappers()


if __name__ == "__main__":
    start_mapper()
    app.run()
