from mongoengine import *

class User(Document):
    pass

class Scroll(Document):
    name = StringField()
    description = StringField()
    owner = ReferenceField(User)
    end = DateTimeField()
    is_finished = BooleanField()


    def validate_me(self):
        errors = []
        if not self.name:
            errors.append('Add name')

        if not self.description:
            errors.append('Add description')

        return errors

    def save_me(self):
        errors = self.validate_me()
        if errors:
            return {'errors':errors}
        else:
            o = self.save()
            return {'id': str(o.id)}



from .user import User
