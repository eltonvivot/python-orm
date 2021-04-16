from mongoengine_goodjson import Document
from mongoengine import StringField, ListField, MapField, BooleanField

class Host(Document):
    name = StringField()
    attributes = ListField(MapField(field=StringField()))
    enabled = BooleanField()
    #host_type_id = db.Column(db.Integer, db.ForeignKey('host_types.id'))
    
    