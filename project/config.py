import os


class BaseConfig(object):
    SECRET_KEY = "thisisnotreallyasecret"
    DEBUG = False


class DevelopmentConfig(object):
    DEBUG = True


class TestingConfig(object):
    DEBUG = False
    TESTING = True
