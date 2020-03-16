# coding: utf-8

# config.py

import os

from dotenv import load_dotenv

# load dotenv
basedir = os.path.abspath(os.path.dirname(__file__))
env = os.path.join(basedir, ".env")
load_dotenv(env)


class Config:

    DEBUG = True
    TESTING = True
    SECRET_KEY = os.getenv("SECRET_KEY")
