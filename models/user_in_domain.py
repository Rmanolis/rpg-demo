from mongoengine import *

class User(Document):
    pass


class Domain(Document):
    pass



class UserInDomain(Document):
    user = ReferenceField(User)
    domain = ReferenceField(Domain)
    accept = BooleanField(default=False)


from .user import User
from .domain import Domain

