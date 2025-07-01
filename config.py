import os
from dotenv import load_dotenv

load_dotenv()

class Config():
    DEBUG = os.environ.get('DEBUG')
    SQLALCHEMY_DATABASE_URI = os.environ.get("SQLALCHEMY_DATABASE_URL")
    SECRET_KEY=os.environ.get("SECRET_KEY")