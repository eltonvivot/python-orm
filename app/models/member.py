from mongoengine_goodjson import Document
from mongoengine import StringField,BooleanField, DatetimeField, IntField, EmbeddedDocumentField
from .ssh_key import SSHKey

class Member(Document):
    name = StringField()
    email = StringField()
    affiliation = StringField()
    password = StringField()  # encriptar
    privilege = IntField()  # definir níveis (documento)
    enabled = BooleanField()
    ssh_key = EmbeddedDocumentField(SSHKey)

