from models.inventory import Inventory
from models.scroll import Scroll
from models.scroll_in_inventory import ScrollInInventory
from library.logic import for_inventory
from library.auth_decorators import authenticate
from flask import *
import settings
import json

logger = settings.logging.getLogger(__name__)

inventory_bp = Blueprint('inventory', __name__)


'''
- Create inventory
- Get scrolls from inventory
- Get inventories
- when you delete inventory,
  you move all the objects to basic inventory
- move scroll from one on inventory to another
'''


@inventory_bp.route('/', methods=['GET','POST'])
@authenticate
def get_post_inventory(user):
    if request.method == 'GET':
        return Inventory.objects(owner=user.id).to_json()

    if request.method == 'POST':
        name = request.json.get('name')
        res = for_inventory.create_inventory(user,name)
        return json.dumps(res)


@inventory_bp.route('/<inventory_id>', methods=['DELETE'])
@authenticate
def delete_inventory(user, inventory_id):
    res = for_inventory.delete_inventory(user, inventory_id)
    return jsonify(res)


@inventory_bp.route('/<inventory_id>/scrolls', methods=['GET'])
@authenticate
def get_scrolls_from_inventory(user,inventory_id):
    inv = Inventory.objects(id=inventory_id,
                            owner=user).first()
    if inv:
        sii_ls = ScrollInInventory.objects(inventory=inv.id)
        scrolls = []
        for sii in sii_ls:
           scroll_obj = Scroll.objects(id=sii.scroll.id).first()
           scroll = {'id': str(scroll_obj.id),
                     'is_finished': scroll_obj.is_finished,
                     'description': scroll_obj.description,
                     'name': scroll_obj.name}
           scrolls.append(scroll)

        return json.dumps(scrolls)
    else:
        return "", 404


@inventory_bp.route('/<from_inv_id>/scrolls/'+\
                    '<scroll_id>/inventories/<to_inv_id>', methods=['PUT'])
@authenticate
def put_scroll_to_another_inventory(user,from_inv_id,
                                    scroll_id,to_inv_id):
    from_inv = Inventory.objects(owner=user.id,
                                 id=from_inv_id).first()
    to_inv = Inventory.objects(owner=user.id,
                               id=to_inv_id).first()
    scroll = Scroll.objects(owner=user.id,
                            id=scroll_id).first()
    if from_inv and to_inv and scroll:
           sii= for_inventory.move_scroll_between_inventories(scroll,
                                                              from_inv,to_inv)
           if sii:
               return "", 202
           else:
               return "", 404
    else:
        return "", 404


