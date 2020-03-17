# coding: utf-8

# tests/test_routes.py

from flask import json


def test_home(client):
    rv = client.get("/")
    assert rv.status_code == 200


def test_login(client):
    data = json.dumps({"username": "user1", "password": "secret1"})
    rv = client.post("/login", data=data, content_type="application/json")
    assert rv.status_code == 200
