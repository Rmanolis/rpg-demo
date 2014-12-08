import logging
import mongoengine

mongoengine.connect("aetherguilds")

logging.basicConfig(level=logging.DEBUG)
                  # format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
                  # datefmt='%m-%d %H:%M',
                  # filename='logs/myapp.log',
                  # filemode='w+')

logging = logging

logger = logging.getLogger()

WEBSOCKET_IP = "http://178.62.126.138:8000"

IMAGE_FOLDER = 'save/images/'
SOUND_FOLDER = 'save/sounds/'

ALLOWED_EXTENSIONS = set([ 'png', 'jpg', 'jpeg', 'gif','mp3', 'wav', 'ogg'])

