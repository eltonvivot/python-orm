from .host import host_bp
from .user import user_bp

def init_app(app):
    app.register_blueprint(host_bp)
    app.register_blueprint(user_bp)