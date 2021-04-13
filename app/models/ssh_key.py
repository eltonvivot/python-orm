from . import db

class SSHKey(db.Model):
    __tablename__ = 'ssh_keys'

    id = db.Column(db.Integer, nullable=False, primary_key=True)
    private_key = db.Column(db.String())
    public_key = db.Column(db.String())

    def __init__(self, private_key, public_key):
        self.private_key = private_key
        self.public_key = public_key