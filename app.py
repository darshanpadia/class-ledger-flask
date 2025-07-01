from flask import Flask
import os
from config import Config
from routes import register_routes
from extensions import db, migrate


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Initialize extensions
    db.init_app(app)
    migrate.init_app(app,db)

    # Import models *after* db is initialized
    from models import Teacher

    # Register routes
    register_routes(app)

    return app