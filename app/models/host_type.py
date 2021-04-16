from mongoengine import Document, StringField, ListField, MapField

class HostType(Document):
    __tablename__ = 'host_types'

    name = StringField()
    attributes = ListField(MapField(field=StringField())) 
