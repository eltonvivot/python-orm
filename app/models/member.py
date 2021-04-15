from . import db

class Member(db.Model):
    __tablename__ = 'members'

    id = db.Column(db.Integer, nullable=False, primary_key=True)
    name = db.Column(db.String())
    email = db.Column(db.String())
    affiliation = db.Column(db.String())
    password = db.Column(db.String())  # encriptar
    privilege = db.Column(db.Integer)  # definir níveis (documento)
    enabled = db.Column(db.Boolean)
    ssh_key_id = db.Column(db.Integer, db.ForeignKey('ssh_keys.id'))
    ssh_key = db.relationship("SSHKey", backref=db.backref(
        "members", uselist=False))  # object reference

    def __init__(self, name, email, affiliation, password, privilege, ssh_key_id, enabled=True, ssh_key=None):
        self.name = name
        self.email = email
        self.affiliation = affiliation
        self.password = password
        self.privilege = privilege
        self.enabled = enabled
        self.ssh_key_id = ssh_key_id
        self.ssh_key = ssh_key
