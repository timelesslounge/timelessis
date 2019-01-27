"""This file contains all functions needed to create
a new Flask app for timeless"""

import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from timeless.companies import views as companies_views


DB = SQLAlchemy()


def create_app(config):
    """Creates a new Timeless webapp given a config class"""
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(config)
    initialize_extensions(app)
    register_endpoints(app)
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
    from timeless.db.schemetypes.scheme_condition import SchemeCondition
    from timeless.companies import models
    from timeless.restaurants import models


def register_endpoints(app):
    app.register_blueprint(companies_views.bp)
