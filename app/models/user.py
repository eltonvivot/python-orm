from mongoengine_goodjson import Document
from mongoengine import StringField

class User(Document):
    name = StringField()
    login = StringField()
    password = StringField()