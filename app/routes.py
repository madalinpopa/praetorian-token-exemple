# coding: utf-8

# app/routes.py

from flask import Blueprint, jsonify, request
from flask_praetorian import auth_required

from app import guard

api = Blueprint("api", __name__)


@api.route("/")
def home():
    return "Hello World!"


@api.route("/login", methods=["POST"])
def login():
    json_data = request.get_json()
    username = json_data["username"]
    password = json_data["password"]
    user = guard.authenticate(username, password)
    token = guard.encode_jwt_token(user)
    return jsonify({"access_token": token})


@api.route("/protected")
@auth_required
def protected():
    return jsonify({"result": "This is a protected page!"})


@api.route("/refresh")
def refresh():
    json_data = request.get_json()
    token = guard.refresh_jwt_token(json_data["token"])
    return jsonify({"access_token": token})
