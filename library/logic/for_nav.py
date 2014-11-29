from library.common import get_user

def sitemap():
    if get_user():
       return [{'url':'#/scrolls',
          'title':'Scrolls'},
         {'url':'#/inventories',
          'title':'Inventories'},
         {'url':'users/logout',
          'title': 'Logout'}]
    else:
        return [{'url':'#/login',
                 'title': 'Login'},
                {'url':'#/register',
                 'title': 'Register'}]

