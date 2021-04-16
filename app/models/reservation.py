from mongoengine import Document, StringField, BooleanField, DatetimeField

class Reservation(Document):
    starts_at = DatetimeField()
    ends_at = DatetimeField()
    enabled = BooleanField()
    # hosts_images_map = db.Column(JSON()) # tratar como relacionamento |-| [{"host": "dell01", "image": "ubuntu"}] 
