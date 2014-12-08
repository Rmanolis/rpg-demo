from mongoengine import *

class Domain(Document):
    pass

class ImageInDomain(Document):
    name = StringField()
    filename = StringField()
    domain = ReferenceField(Domain)
    type_of_image = StringField()
    disk_url = StringField()

from .domain import Domain
