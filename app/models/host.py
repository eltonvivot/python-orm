from mongoengine_goodjson import Document
from mongoengine import signals, StringField, ListField, MapField, BooleanField, ReferenceField
from.host_type import HostType

class Host(Document):
    name = StringField()
    attributes = ListField(MapField(field=StringField()))
    enabled = BooleanField()
    host_type = ReferenceField(HostType)

    @classmethod
    def pre_save(cls, sender, document, **kwargs):
        document.host_type

signals.pre_save.connect(Host.pre_save, sender=Host)