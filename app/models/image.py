from mongoengine import Document, StringField, ListField, MapField, BooleanField


class Image(Document):
    __tablename__ = 'images'

    name = StringField()
    attributes = ListField(MapField(field=StringField())) 
    # reservation_id = db.Column(db.Integer, db.ForeignKey('reservations.id'))

