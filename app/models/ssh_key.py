from mongoengine_goodjson import EmbeddedDocument
from mongoengine import StringField

class SSHKey(EmbeddedDocument):
    private_key = StringField()
    public_key = StringField()