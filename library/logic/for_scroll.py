from datetime import datetime
from datetime import timedelta
from models.scroll import Scroll
from models.inventory import Inventory
from models.scroll_in_inventory import ScrollInInventory
import requests
import settings
def create_scroll(user, name, description):
    scroll = Scroll()
    scroll.name = name
    scroll.description = description
    scroll.end = datetime.now() + timedelta(minutes=5)
    scroll.owner = user.to_dbref()
    scroll.is_finished = False
    return scroll.save_me()


def check_for_finished_scrolls():
    for scroll in Scroll.objects(is_finished=False):
        current_time = datetime.now()
        if scroll.end <= current_time:
            print('Scroll name ' + scroll.name)
            scroll.is_finished = True
            scroll.save()
            inv = Inventory.objects(owner=scroll.owner.id,
                              is_basic=True).first()
            sii = ScrollInInventory()
            sii.scroll=scroll.to_dbref()
            sii.inventory= inv.to_dbref()
            sii.save()
            #inform user with node.js
            payload = {'user_id': str(scroll.owner.id),
                       'scroll_name': scroll.name}
            requests.post(settings.WEBSOCKET_IP +'/scrolls/ready' ,data=payload)
