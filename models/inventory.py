from mongoengine import *

class User(Document):
    pass

class Inventory(Document):
    name = StringField()
    owner = ReferenceField(User)
    is_basic= BooleanField(default=False)

    def validate_me(self):
        errors = []
        if self.name.lower() == 'basic':
            errors.append('This name is occupied , sorry!')

        if not self.name:
            errors.append("The name can not be empty")

        return errors

    def save_me(self):
        errors = self.validate_me()
        if errors:
            return {'errors':errors}
        else:
            o = self.save()
            return {'id':str(o.id)}

from .user import User
