from flask import *
from functools import wraps

from .common import get_user

def authenticate(f):
    @wraps(f)
    def inner(*args, **kwargs):
        user = get_user()
        if user:
            res = f(user, *args, **kwargs)
            return res
        else:
            return "", 403
    return inner

