from flask import *
from library.logic import for_nav
from library.logic import for_scroll
import settings
import os
from controllers.inventory_ctrl import inventory_bp
from controllers.scroll_ctrl import scroll_bp
from controllers.user_ctrl import user_bp
from controllers.domain_ctrl import domain_bp
import threading
from datetime import datetime
from flask_oauthlib.client import OAuth, OAuthException

FACEBOOK_APP_ID = '669039869884239'
FACEBOOK_APP_SECRET = '7e9fe10ceb4a408e7137334ea7434da5'

app = Flask(__name__)
app.secret_key = 'secret!'
app.config['DEBUG'] = True

app._static_folder = 'public'
app.register_blueprint(user_bp, url_prefix='/users')
app.register_blueprint(scroll_bp, url_prefix='/scrolls')
app.register_blueprint(inventory_bp, url_prefix="/inventories")
app.register_blueprint(domain_bp, url_prefix="/domains")
oauth = OAuth(app)

facebook = oauth.remote_app(
    'facebook',
    consumer_key=FACEBOOK_APP_ID,
    consumer_secret=FACEBOOK_APP_SECRET,
    request_token_params={'scope': 'email'},
    base_url='https://graph.facebook.com',
    request_token_url=None,
    access_token_url='/oauth/access_token',
    authorize_url='https://www.facebook.com/dialog/oauth'
)





@app.route('/')
def login():
    callback = url_for(
        'facebook_authorized',
        next=request.args.get('next') or request.referrer or None,
        _external=True
    )
    return facebook.authorize(callback=callback)


@app.route('/login/authorized')
def facebook_authorized():
    resp = facebook.authorized_response()
    if resp is None:
        return 'Access denied: reason=%s error=%s' % (
            request.args['error_reason'],
            request.args['error_description']
        )
    if isinstance(resp, OAuthException):
        return 'Access denied: %s' % resp.message

    session['oauth_token'] = (resp['access_token'], '')
    me = facebook.get('/me')
    return 'Logged in as id=%s name=%s redirect=%s' % \
        (me.data['id'], me.data['name'], request.args.get('next'))




@app.route('/sitemap',methods=['GET'])
def get_sitemap():
    return json.dumps(for_nav.sitemap())

def time_loader():
  threading.Timer(60, time_loader).start ()
  print('Loader start ' + str(datetime.now()) )
  for_scroll.check_for_finished_scrolls()
  print('Loader finished ' + str(datetime.now()))

#time_loader()

if __name__ == "__main__":
    app.run(host = '0.0.0.0' , port=5051)

