import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app(config):
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
    db.init_app(app)
    from .models import Company
