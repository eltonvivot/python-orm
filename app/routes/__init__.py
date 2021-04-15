from .ssh_key import ssh_key_bp

def init_app(app):
    app.register_blueprint(ssh_key_bp)