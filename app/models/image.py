from . import db
from sqlalchemy.dialects.postgresql import JSON # json type 

class Image(db.Model):
    __tablename__ = 'images'

    id = db.Column(db.Integer, nullable=False, primary_key=True)
    name = db.Column(db.String())
    attributes = db.Column(JSON())

    host_id = db.Column(db.Integer, db.ForeignKey('host.id'))
    reservation_id = db.Column(db.Integer, db.ForeignKey('reservations.id'))

    def __init__(self, name, attributes):
        self.name = name
        self.attributes = attributes