from . import db
from sqlalchemy.dialects.postgresql import JSON # json type 

class Reservation(db.Model):
    __tablename__ = 'reservations'

    id = db.Column(db.Integer, nullable=False, primary_key=True)
    starts_at = db.Column(db.Datetime())
    ends_at = db.Column(db.Datetime())
    enabled = db.Column(db.Boolean)

    hosts_images_map = db.Column(JSON()) # definir função para tratar |-| [{"host": "dell01", "image": "ubuntu"}] 

    def __init__(self, starts_at, ends_at, enabled=True, hosts_images_map=None):
        self.starts_at = starts_at
        self.ends_at = ends_at
        self.enabled = enabled
        self.hosts_images_map = hosts_images_map