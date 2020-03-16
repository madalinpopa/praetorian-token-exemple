# coding: utf-8

# app/routes.py

from flask import Blueprint, jsonify, request

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
    print(user)
    token = guard.encode_jwt_token(user)
    print(token)
    return jsonify({"access_token": token})
