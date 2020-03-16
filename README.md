# Example of ussage of flask-praetorian extension

This is a simple example of of usage of flask-praetorian extension with flask. 

Within this example I have used **sqlalchemy.orm** instead of Flask-SQLAlchemy.

### Instalation

1. Clone the repository
2. Create an `.env` file with `SECRET_KEY`
3. Create an `.flaskenv` file with the following variables
    - `FLASK_APP=wsgi`
    - `FLASK_ENV=development`
4. Run the following `pip install -r requirements.txt`
5. Run the application `flask run`