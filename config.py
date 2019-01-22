import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SECRET_KEY = 'timele$$i$'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
class ProductionConfig(Config):
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = 'postgresql://timeless_user:timeless_pwd@localhost/timelessdb'


class StagingConfig(Config):
    DEVELOPMENT = True
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'postgresql://timeless_user:timeless_pwd@localhost/timelessdb_dev'


class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'postgresql://timeless_user:timeless_pwd@localhost/timelessdb_dev'


class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'postgresql://timeless_user:timeless_pwd@localhost/timelessdb_test'
