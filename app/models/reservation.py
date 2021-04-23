from mongoengine_goodjson import Document, EmbeddedDocument
from mongoengine import signals, StringField, BooleanField, DateTimeField, ReferenceField, EmbeddedDocumentListField
from .host import Host
from .image import Image

class HostImage(EmbeddedDocument):
    host = ReferenceField(Host)
    image = ReferenceField(Image)

class Reservation(Document):
    starts_at = DateTimeField()
    ends_at = DateTimeField()
    enabled = BooleanField()
    hosts_images = EmbeddedDocumentListField(HostImage) # [{"host": "dell01", "image": "ubuntu"}]

    @classmethod
    def pre_save(cls, sender, document, **kwargs):
        for hosts_images in document.hosts_images:
            hosts_images.host
            hosts_images.image

signals.pre_save.connect(Reservation.pre_save, sender=Reservation)