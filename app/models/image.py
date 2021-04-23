from mongoengine_goodjson import Document
from mongoengine import StringField, ListField, MapField, BooleanField

class Image(Document):
    name = StringField()
    attributes = ListField(MapField(field=StringField())) 
