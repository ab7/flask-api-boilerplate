import os
basedir = os.path.abspath(os.path.dirname(__file__))


class ConfigBase:
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SECRET_KEY = 'change_this'
    SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']


class ConfigProduction(ConfigBase):
    DEBUG = False


class ConfigStage(ConfigBase):
    DEVELOPMENT = True
    DEBUG = True


class ConfigDevelopment(ConfigBase):
    DEVELOPMENT = True
    DEBUG = True


class ConfigTest(ConfigBase):
    TESTING = True
