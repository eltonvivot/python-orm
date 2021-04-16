from mongoengine import Document, StringField,BooleanField, DatetimeField, IntField

class Member(Document):
    name = StringField()
    email = StringField()
    affiliation = StringField()
    password = StringField()  # encriptar
    privilege = IntField()  # definir níveis (documento)
    enabled = BooleanField()
    # ssh_key_id = db.Column(db.Integer, db.ForeignKey('ssh_keys.id'))

