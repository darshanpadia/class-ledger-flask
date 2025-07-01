import os

class Config():
    DEBUG = os.environ.get('DEBUG')
    SQLALCHEMY_DATABASE_URI = os.environ.get("SQLALCHEMY_DATABASE_URL")