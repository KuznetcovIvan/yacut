from os import getenv


class Config(object):
    SQLALCHEMY_DATABASE_URI = getenv('DATABASE_URI')
    SECRET_KEY = getenv('SECRET_KEY')
