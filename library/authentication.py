from models.user import User
from models.inventory import Inventory
from flask import session

def login(email, password):
    user = User.authenticate(email, password)
    if user:
        session['user_id'] = str(user.id)
        return { 'is_accepted': True,
                'message':'User accepted'}
    else:
        return {'is_accepted':False,
                'message': 'Wrong email and password'}




def register(email, username, password):
    user = User()
    user.email = email
    user.username = username
    user.password = password
    errors = user.validate_me()
    if errors:
        print(errors)
        return {'errors': errors}
    else:
        res = user.save_me()
        if 'id' in res.keys():
            user = User.objects(id=res['id']).first()
            Inventory(owner=user.to_dbref(),
                      name='Basic',
                      is_basic=True).save()
        return res

