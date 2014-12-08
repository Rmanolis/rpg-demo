from mongoengine import *

class User(Document):
    pass

class Domain(Document):
    name = StringField()
    user = ReferenceField(User)

    def validate_me(self):
        errors = []
        if not self.name:
            errors.append("Add name")
        return errors

    def save_me(self):
        errors = self.validate_me()
        if errors:
            return {'errors':errors}
        else:
            o = self.save()
            return {'id': str(o.id)}

from .user import User
