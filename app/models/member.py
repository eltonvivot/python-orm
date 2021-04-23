from mongoengine_goodjson import Document
from mongoengine import StringField, BooleanField, IntField, EmbeddedDocumentField
from .ssh import SSHKey

class Member(Document):
    name = StringField()
    email = StringField()
    affiliation = StringField()
    password = StringField()  # encriptar
    privilege = IntField()  # definir níveis (documento)
    enabled = BooleanField()
    ssh_key = EmbeddedDocumentField(SSHKey)
