from . import db
from sqlalchemy.dialects.postgresql import JSON  # json type

class HostType(db.Model):
    __tablename__ = 'host_types'

    id = db.Column(db.Integer, nullable=False, primary_key=True)
    name = db.Column(db.String())
    attributes = db.Column(JSON())

    def __init__(self, name, attributes):
        self.name = name
        self.attributes = attributes
