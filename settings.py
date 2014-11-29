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

WEBSOCKET_IP = "http://127.0.0.1:8001"

