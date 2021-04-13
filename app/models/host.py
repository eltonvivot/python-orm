from . import db
from sqlalchemy.dialects.postgresql import JSON # json type 

class Host(db.Model):
    __tablename__ = 'hosts'

    id = db.Column(db.Integer, nullable=False, primary_key=True)
    name = db.Column(db.String())
    attributes = db.Column(JSON())
    enabled = db.Column(db.Boolean)
    host_type_id = db.Column(db.Integer, db.ForeignKey('host_types.id'))
    # testing object reference
    host_type = relationship("HostType", backref=backref("hosts", uselist=False))

    def __init__(self, name, attributes, enabled, host_type=None):
        self.name = name
        self.attributes = attributes
        self.enabled = enabled
        self.host_type = host_type