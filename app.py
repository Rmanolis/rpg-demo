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
from library import facebook

app = Flask(__name__)
app._static_folder = 'public'
app.register_blueprint(user_bp, url_prefix='/users')
app.register_blueprint(scroll_bp, url_prefix='/scrolls')
app.register_blueprint(inventory_bp, url_prefix="/inventories")
app.register_blueprint(domain_bp, url_prefix="/domains")

app.config.update({
    'DEBUG': True,
    'CANVAS_CLIENT_ID': '669039869884239',
    'CANVAS_CLIENT_SECRET': '7e9fe10ceb4a408e7137334ea7434da5',
    'CANVAS_REDIRECT_URI': 'http://apps.facebook.com/remodmaomo/',
    'CANVAS_SCOPE': 'email',
    'CANVAS_ERROR_URI': '/error'
})

facebook.install(app)

app.secret_key = 'secret!'



@app.route("/")
def index():
    return send_file('public/index.html')




@app.canvas_route('/user',
                  methods=['POST'])
def fb_user(canvas_user):
    return canvas_user.request('/me')

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

