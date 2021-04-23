from mongoengine_goodjson import Document
from mongoengine import StringField, BooleanField, DatetimeField

class Project(Document):
    name = StringField()
    expiration_date = DatetimeField()
    enabled = BooleanField()

    
    # owner_id = db.Column(db.Integer, db.ForeignKey('members.id'))
    # owner = db.relationship("Member", backref=db.backref("projects", uselist=False)) # object reference
    # participants = db.relationship("Member", secondary=projects_participants_association) # participants reference
    # requested_accesses = db.relationship("Member", secondary=projects_requested_accesses_association) # requested_accesses reference
