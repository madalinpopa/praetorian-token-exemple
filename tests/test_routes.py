# coding: utf-8

# tests/test_routes.py

from flask import json
from app.model import User
from app.database import db_test_session
from app.orm import start_mapper

import os
from dotenv import load_dotenv


def test_home(client):
    rv = client.get("/")
    assert rv.status_code == 200
    assert b"Hello World!" in rv.data


def test_login(client):
    data = json.dumps({"username": "user1", "password": "secret1"})
    rv = client.post("/login", data=data, content_type="application/json")
    json_data = rv.get_json()
    assert "eyJ0eXAiOiJK" in json_data["access_token"]
    assert rv.status_code == 200


def test_protected(client):
    data = json.dumps({"username": "user1", "password": "secret1"})
    rv = client.post("/login", data=data, content_type="application/json")
    json_data = rv.get_json()
    headers = {"Authorization": "Bearer " + json_data["access_token"]}
    rv = client.get("/protected", headers=headers)
    assert rv.status_code == 200
