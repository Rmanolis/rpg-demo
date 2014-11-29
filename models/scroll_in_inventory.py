from mongoengine import *

class Scroll(Document):
    pass

class Inventory(Document):
    pass

class ScrollInInventory(Document):
    scroll = ReferenceField(Scroll)
    inventory = ReferenceField(Inventory)

from .scroll import Scroll
from .inventory import Inventory
