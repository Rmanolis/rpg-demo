from models.inventory import Inventory
from models.scroll_in_inventory import ScrollInInventory

def create_inventory(user, name):
    inv = Inventory()
    inv.owner = user.to_dbref()
    inv.name = name
    return inv.save_me()


def delete_inventory(user, inv):
    errors = []
    success = False
    inv = Inventory.objects(owner=user.id,
                            id = id).first()
    if inv:
        if inv.is_basic:
            errors.append('You can not delete this inventory')
        else:
            move_all_scrolls_to_basic(user,inv)
            inv.delete()
            success = True
    else:
        errors.append("This inventory is not yours")

    return {'success':success, 'errors':errors}


def move_all_scrolls_to_basic(user, from_inventory):
    basic_inventory = Inventory.objects(owner=user.id,
                                        is_basic=True).first()
    sii_ls = ScrollInInventory.objects(inventory=from_inventory.id)
    for sii in sii_ls:
        sii.inventory = basic_inventory.to_dbref()
        sii.save()

def move_scroll_between_inventories(scroll,from_inv, to_inv):
    sii = ScrollInInventory.objects(scroll=scroll.id,
                              inventory=from_inv.id).first()
    if sii:
        sii.inventory = to_inv.to_dbref()
        sii.save()
        return sii
    else:
        return None


