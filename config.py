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
    REDIS_HOST = "redis://localhost:6379"
    RESULT_BACKEND = REDIS_HOST
    BROKER_URL = REDIS_HOST


class StagingConfig(Config):
    DEVELOPMENT = True
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = os.environ.get(
        "SQLALCHEMY_DATABASE_URI",
        "postgresql://timeless_user:timeless_pwd@localhost/timelessdb_dev")
    REDIS_HOST = "redis://localhost:6379"
    RESULT_BACKEND = REDIS_HOST
    BROKER_URL = REDIS_HOST


class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get(
        "SQLALCHEMY_DATABASE_URI",
        "postgresql://timeless_user:timeless_pwd@localhost/timelessdb_dev")
    REDIS_HOST = "redis://localhost:6379"
    RESULT_BACKEND = REDIS_HOST
    BROKER_URL = REDIS_HOST



class TestingConfig(Config):
    TESTING = True
    WTF_CSRF_ENABLED = False
    SQLALCHEMY_DATABASE_URI = os.environ.get(
        "SQLALCHEMY_DATABASE_URI",
        "postgresql://timeless_user:timeless_pwd@localhost/timelessdb_test")
    REDIS_HOST = "redis://localhost:6379"
    RESULT_BACKEND = REDIS_HOST
    BROKER_URL = REDIS_HOST
    