from . import db
from sqlalchemy.dialects.postgresql import JSON  # json type

class Image(db.Model):
    __tablename__ = 'images'

    id = db.Column(db.Integer, nullable=False, primary_key=True)
    name = db.Column(db.String())
    attributes = db.Column(JSON())
    reservation_id = db.Column(db.Integer, db.ForeignKey('reservations.id'))

    def __init__(self, name, attributes, reservation_id):
        self.name = name
        self.attributes = attributes
        self.reservation_id = reservation_id
