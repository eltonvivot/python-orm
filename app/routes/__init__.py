from .resource import resource_bp
from .user import user_bp

def init_app(app):
    #app.register_blueprint(user_bp)
    app.register_blueprint(resource_bp)