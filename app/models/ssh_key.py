from mongoengine import Document, StringField

class SSHKey(Document):
    private_key = StringField()
    public_key = StringField()

