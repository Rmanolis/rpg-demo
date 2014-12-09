from models.scroll import Scroll
from flask import *
from library.auth_decorators import authenticate, jsonp
from library.logic import for_scroll
import settings
import json
from datetime import datetime

logger = settings.logging.getLogger(__name__)

scroll_bp = Blueprint('scroll', __name__)

'''
  - Create scroll
  - Get scroll
  - when created after 5 min add to basic inventory of the owner
'''


@scroll_bp.route('/', methods=['POST'])
@authenticate
@jsonp
def post_scroll(user):
    name = request.json.get('name')
    description = request.json.get('description')
    res = for_scroll.create_scroll(user,name,description)
    return jsonify(res)

@scroll_bp.route('/<scroll_id>', methods=['GET'])
@authenticate
@jsonp
def get_scroll(user, scroll_id):
    scroll = Scroll.objects(user=user,
                   id=scroll_id).first()
    if scroll:
        return scroll.to_json()
    else:
        return "", 404


@scroll_bp.route('/unfinished', methods=['GET'])
@authenticate
@jsonp
def get_unfinished_scrolls(user):
    scrolls = []
    sc_ls = Scroll.objects(owner=user, is_finished=False)
    for sc in sc_ls:
        now = datetime.now()
        if sc.end > now:
            td = sc.end - datetime.now()
            scroll = {}
            scroll['id'] = str(sc.id)
            scroll['name'] = sc.name
            scroll['seconds_remain'] = td.seconds
            scrolls.append(scroll)

    return json.dumps(scrolls)

