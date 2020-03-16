# coding: utf-8

# wsgi.py

from app import create_app
from app.database import Session, engine
from app.orm import metadata, start_mapper

app = create_app()


@app.teardown_appcontext
def cleanup(resp_or_exception):
    Session.remove()


if __name__ == "__main__":
    start_mapper()
    metadata.create_all(bind=engine)
    app.run()
