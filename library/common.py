from flask import *
from models.user import User

def get_user_id():
    try:
        key = session['user_id']
    except KeyError:
        key = None
    return key

def get_user():
    id = get_user_id()
    if id:
        u = User.objects(id=id).first()
        return u
    else:
        return None
