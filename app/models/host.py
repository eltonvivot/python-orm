from mongoengine_goodjson import Document
from mongoengine import StringField, ListField, MapField, BooleanField

class Host(Document):
    name = StringField()
    attributes = ListField(MapField(field=StringField()))
    enabled = BooleanField()
    #host_type_id = db.Column(db.Integer, db.ForeignKey('host_types.id'))

    def serialize(self, data):
        self.name = data["name"]
        self.attributes = data["attributes"]
        self.enabled = data["enabled"]
    
    def to_json(self):
        return {"name": self.name,
                "attributes": self.attributes,
                "enabled": self.enabled}
    