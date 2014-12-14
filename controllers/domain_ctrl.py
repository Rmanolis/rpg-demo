from flask import *
from models.domain import Domain
from models.user import User
from models.user_in_domain import UserInDomain
from models.file_in_domain import FileInDomain
from library.auth_decorators import authenticate
from library.logic import for_domain
from library.json_encoder import JsonEncoder
import settings
logger = settings.logging.getLogger(__name__)

domain_bp = Blueprint('domain', __name__)

@domain_bp.route('/', methods=['GET','POST'])
@authenticate
def post_domain(user):
    if request.method == 'GET':
        domains = Domain.objects.to_json()
        return domains

    if request.method == 'POST':
        name = request.json.get('name')
        return jsonify(for_domain.add_domain(user,name))



@domain_bp.route('/<domain_id>/files/',
                 methods=['POST'])
@authenticate
def post_file_domain(user, domain_id):
        file = request.files['file']
        name = request.form.get('name')
        type_of_file = request.form.get('type_of_file')
        if not name :
            return "Add name", 403
        if not type_of_file :
            return "Add type of file", 403
        domain = Domain.objects(id=domain_id,
                                user=user.id).first()
        if domain:
            dm = for_domain.add_file_to_domain(domain,
                                          file,
                                          name,
                                          'files',
                                          type_of_file)

            if not dm:
                return "", 202
            else:
                return dm , 403
        else:
            return "" , 404

@domain_bp.route('/<domain_id>/type_of_files/<file_type>/files')
@authenticate
def get_files_by_type(user, domain_id, file_type):
    domain = Domain.objects(id=domain_id,
                            user=user.id).first()
    if domain:
       res= FileInDomain.objects(domain=domain.id,
                     type_of_file=file_type).all().to_json()
       return res
    else:
        return "",404




@domain_bp.route('/<domain_id>/files/<file_id>',
                 methods=['PUT','GET'])
@authenticate
def put_file_domain(user, domain_id, file_id):
    domain = Domain.objects(id=domain_id).first()
    if domain:
       fid = FileInDomain.objects(domain=domain.id,
                             id=file_id).first()
       if fid:
            if request.method == 'PUT':
                name = request.json.get('name')
                fid.name = name
                res = fid.save_me()
                if 'errors' in res.keys():
                    return jsonify(res), 403
                else:
                    return jsonify(res)
            else:
                print(fid.filename)
                return send_file('files/'+fid.filename)
       else:
           return "", 404
    else:
        return "", 404


@domain_bp.route('/<domain_id>', methods=["PUT","GET"])
@authenticate
def put_domain_field(user, domain_id):
    domain = Domain.objects(id=domain_id).first()
    if domain:
        if request.method == "PUT":
            name = request.json.get('name')
            domain.name = name
            res = domain.save_me()
            if 'errors' in res.keys():
                return jsonify(res), 403
            else:
                return jsonify(res)
        if request.method == "GET":
            return domain.to_json()
    else:
        return "", 404

@domain_bp.route('/<domain_id>/connect')
@authenticate
def user_connect_to_domain(user, domain_id):
    domain = Domain.objects(id=domain_id).first()
    if domain and domain.user.id != user.id:
        uid = UserInDomain.objects(domain=domain.id,
                             user=user.id).first()
        if not uid:
            uid = UserInDomain()
            uid.user = user.to_dbref()
            uid.domain = domain.to_dbref()
            uid.save()
        return "", 202
    else:
        return "", 404


@domain_bp.route('/<domain_id>/quit')
@authenticate
def user_quit_from_domain(user, domain_id):
    domain = Domain.objects(id=domain_id).first()
    if domain and domain.user.id != user.id:
        uid = UserInDomain(domain=domain.id,
                           user=user.id).first()
        if uid:
            uid.delete()
        return "", 202
    else:
        return "", 404



@domain_bp.route('/<domain_id>/users')
@authenticate
def get_domain_users(user, domain_id):
    domain = Domain.objects(id=domain_id).first()
    users = []
    if domain:
        uid_ls = UserInDomain.objects(domain=domain.id).all()
        for uid in uid_ls:
            user = User.objects(id=uid.user.id).first()
            users.append({'username':user.username,
                          'id':str(user.id)})
    return json.dumps(users)
