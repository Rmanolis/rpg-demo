from flask import *
from library.logic import for_nav
from library.logic import for_scroll
import settings
import os
from controllers.inventory_ctrl import inventory_bp
from controllers.scroll_ctrl import scroll_bp
from controllers.user_ctrl import user_bp
import threading
from datetime import datetime

app = Flask(__name__)
app._static_folder = 'public'
app.register_blueprint(user_bp, url_prefix='/users')
app.register_blueprint(scroll_bp, url_prefix='/scrolls')
app.register_blueprint(inventory_bp, url_prefix="/inventories")


app.config['DEBUG'] = True
app.secret_key = 'secret!'


@app.route("/")
def index():
    return send_file('public/index.html')




@app.route('/sitemap',methods=['GET'])
def get_sitemap():
    return json.dumps(for_nav.sitemap())

def time_loader():
  threading.Timer(60, time_loader).start ()
  print('Loader start ' + str(datetime.now()) )
  for_scroll.check_for_finished_scrolls()
  print('Loader finished ' + str(datetime.now()))

time_loader()

if __name__ == "__main__":
    app.run(host = '0.0.0.0' , port=5051)

