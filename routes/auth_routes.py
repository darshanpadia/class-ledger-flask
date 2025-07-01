from flask import Blueprint

auth_routes = Blueprint('auth_routes', __name__)

@auth_routes.route('/')
def home():
    return "Jello"