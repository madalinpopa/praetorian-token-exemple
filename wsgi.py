# coding: utf-8

# wsgi.py

from app import create_app
from app.orm import start_mapper
from app.database import db_session
from manage import init_prod, init_test, testdb

app = create_app()

app.cli.add_command(init_prod)
app.cli.add_command(init_test)
app.cli.add_command(testdb)


@app.before_first_request
def start_model_mapper():
    start_mapper()


@app.teardown_appcontext
def cleanup(resp_or_exception):
    db_session.remove()


if __name__ == "__main__":
    app.run()
