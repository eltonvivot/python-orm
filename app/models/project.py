from . import db

projects_participants_association = db.Table(
    'projects_participants', db.metadata,
    db.Column('project_id', db.Integer, db.ForeignKey('projects.id')),
    db.Column('member_id', db.Integer, db.ForeignKey('member.id'))
    #db.Column('role', db.String())
)

projects_requested_accesses_association = db.Table(
    'projects_requested_accesses', db.metadata,
    db.Column('project_id', db.Integer, db.ForeignKey('projects.id')),
    db.Column('member_id', db.Integer, db.ForeignKey('member.id'))
    #db.Column('justificativa', db.String())
)

class Project(db.Model):
    __tablename__ = 'projects'

    id = db.Column(db.Integer, nullable=False, primary_key=True)
    name = db.Column(db.String())
    expiration_date = db.Column(db.Datetime)
    enabled = db.Column(db.Boolean)

    owner_id = db.Column(db.Integer, db.ForeignKey('members.id'))
    owner = db.relationship("Member", backref=db.backref("projects", uselist=False)) # object reference
    participants = db.relationship("Member", secondary=projects_participants_association) # participants reference
    requested_accesses = db.relationship("Member", secondary=projects_requested_accesses_association) # requested_accesses reference

    def __init__(self, name, expiration_date, enabled, owner_id, owner=None, participants=None, requested_accesses=None):
        self.name = name
        self.expiration_date = expiration_date
        self.enabled = enabled 
        self.owner_id = owner_id
        self.owner = owner
        self.participants = participants
        self.requested_accesses = requested_accesses