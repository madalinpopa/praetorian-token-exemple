# coding: utf-8

# app/model.py


class User:
    def __init__(self, username: str, password: str):
        self.username = username
        self.password = password
        self.roles: str
        self.id: int

    def __repr__(self):
        return f"<User: {self.username}>"

    @property
    def identity(self):
        return self.id

    @property
    def rolenames(self):
        return []

    @property
    def password(self):
        return self.password

    @classmethod
    def lookup(cls, username):
        return cls.query.filter_by(username=username).one_or_none()

    @classmethod
    def identify(cls, id):
        return cls.query.get(id)
