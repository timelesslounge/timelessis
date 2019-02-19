import os


basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SECRET_KEY = "timele$$i$"
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class ProductionConfig(Config):
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = os.environ.get(
        "SQLALCHEMY_DATABASE_URI",
        "postgresql://timeless_user:timeless_pwd@localhost/timelessdb")
    RESULT_BACKEND = "redis://localhost:6379"
    BROKER_URL = "redis://localhost:6379"
    REDIS_HOST = "localhost"


class StagingConfig(Config):
    DEVELOPMENT = True
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get(
        "SQLALCHEMY_DATABASE_URI",
        "postgresql://timeless_user:timeless_pwd@localhost/timelessdb_dev")
    RESULT_BACKEND = "redis://localhost:6379"
    BROKER_URL = "redis://localhost:6379"
    REDIS_HOST = "localhost"


class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get(
        "SQLALCHEMY_DATABASE_URI",
        "postgresql://timeless_user:timeless_pwd@localhost/timelessdb_dev")
    RESULT_BACKEND = "redis://localhost:6379"
    BROKER_URL = "redis://localhost:6379"
    REDIS_HOST = "localhost"



class TestingConfig(Config):
    RESULT_BACKEND = "redis://localhost:6379"
    BROKER_URL = "redis://localhost:6379"
    TESTING = True
    WTF_CSRF_ENABLED = False
    REDIS_HOST = "localhost"
    SQLALCHEMY_DATABASE_URI = os.environ.get(
        "SQLALCHEMY_DATABASE_URI",
        "postgresql://timeless_user:timeless_pwd@localhost/timelessdb_test")

