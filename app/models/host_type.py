from mongoengine_goodjson import Document
from mongoengine import StringField, ListField, MapField

#host_types -> HostType
class HostType(Document):
    name = StringField()
    attributes = ListField(MapField(field=StringField())) 
