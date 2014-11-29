from models.user import User
from flask import *
from library.auth_decorators import authenticate
from library.authentication import login, register
from library.common import get_user
import settings

logger = settings.logging.getLogger(__name__)

user_bp = Blueprint('user', __name__)

@user_bp.route('/login', methods=['POST'])
def post_login():
    try:
        user = request.json
        return jsonify(login(**user))
    except Exception as e:
        logger.exception(e)
        return "", 403


@user_bp.route('/logout', methods=['GET'])
@authenticate
def get_logout(user):
    session.clear()
    return redirect('/#/login')


@user_bp.route('/is/in', methods=['GET'])
def get_is_in():
    if get_user():
        return "", 200
    else:
        return "", 403


@user_bp.route('/current', methods=['GET'])
@authenticate
def get_current(user):
    return jsonify({'username':user.username,
                    'id': str(user.id)})

@user_bp.route('/register', methods=['POST'])
def post_register():
    email = request.json.get('email')
    username = request.json.get('username')
    password = request.json.get('password')
    res = register(email, username, password)
    return jsonify(res)




