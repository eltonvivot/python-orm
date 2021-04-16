from mongoengine_goodjson import Document
from mongoengine import StringField, ListField, MapField


class HostType(Document):
    name = StringField()
    attributes = ListField(MapField(field=StringField())) 
