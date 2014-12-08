'''from mongoengine import *

class User(Document):
    pass

class Skill(Document):
    pass

class Domain(Document):
    pass

class ActionInDomain(Document):
    domain = ReferenceField(Domain)
    user = ReferenceField(User)
    skill = ReferenceField(Skill)


from .domain import Domain
from .user_skill import Skill'''
