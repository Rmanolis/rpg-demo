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




def jsonp(func):
    """Wraps JSONified output for JSONP requests."""
    @wraps(func)
    def decorated_function(*args, **kwargs):
        callback = request.args.get('callback', False)
        if callback:
            data = str(func(*args, **kwargs).data)
            content = str(callback) + '(' + data + ')'
            mimetype = 'application/javascript'
            return current_app.response_class(content, mimetype=mimetype)
        else:
            return func(*args, **kwargs)
    return decorated_function
