from flask import Flask
import os
from config import Config
from routes import register_routes
from extensions import db, migrate, csrf
from services.teacher_services import add_default_teachers


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Initialize extensions
    db.init_app(app)
    migrate.init_app(app,db)
    csrf.init_app(app)

    # Import models *after* db is initialized to avoid circular imports
    from models import Teacher, StudentRecord, EditLog

    register_routes(app)

    with app.app_context():
        db.create_all()         # Creates all the db tables
        add_default_teachers()  # Add default teachers for testing

    return app