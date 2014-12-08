from mongoengine import *

class Domain(Document):
    pass

class FileInDomain(Document):
    name = StringField()
    filename = StringField()
    domain = ReferenceField(Domain)
    type_of_file = StringField()
    disk_url = StringField()
    extension = StringField()

from .domain import Domain
