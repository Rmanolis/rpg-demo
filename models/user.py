from mongoengine import *
from passlib.apps import custom_app_context

class User(Document):
    email = StringField(required=True)
    username = StringField(required=True)
    password = StringField(required=True)

    def show(self):
        return { 'username': self.username}

    @classmethod
    def encrypt(cls, password):
        password_hash = custom_app_context.encrypt(password)
        return password_hash

    @classmethod
    def verify_password(cls, password, password_hash):
        return custom_app_context.verify(password, password_hash)

    @classmethod
    def authenticate(cls, email, password):
        user = User.objects(email=email).first()
        if user:
            if cls.verify_password(password, user.password):
                return user
            else:
                return None
        else:
            return None

    def validate_me(self):
        errors = []
        if User.objects(email=self.email):
            errors.append('The email is not unique')

        if User.objects(username=self.username):
            errors.append('The username is not unique')

        if not '@' in self.email:
            errors.append('Add correct email')

        if not self.password:
            errors.append('Add password')

        if not self.username:
            errors.append('Add username')

        return errors


    def save_me(self, save_password=True):
        if save_password:
            pwd = self.password
            hashed = User.encrypt(pwd)
            self.password = hashed
        errors = self.validate_me()
        if errors:
            return {'errors': errors}
        else:
            print('lalal')
            u = self.save()
            return {'id': str(u.id)}

