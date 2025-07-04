from .auth_routes import auth_routes
from .dashboard_routes import dashboard_routes

def register_routes(app):
    '''Register all route blueprints to app (Flask aplication instance)'''
    app.register_blueprint(auth_routes)
    app.register_blueprint(dashboard_routes)