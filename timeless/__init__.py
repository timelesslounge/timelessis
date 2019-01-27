"""This file contains all functions needed to create
a new Flask app for timeless"""

import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

DB = SQLAlchemy()

def create_app(config):
    """Creates a new Timeless webapp given a config class"""
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(config)
    initialize_extensions(app)
    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass
    @app.route('/')
    def main():
        return 'Hello, World!'
    return app

def initialize_extensions(app):
    """Initialize extensions for the app"""
    DB.init_app(app)
    from .models import Company
    from timeless.db.schemetypes.scheme_condition import SchemeCondition
