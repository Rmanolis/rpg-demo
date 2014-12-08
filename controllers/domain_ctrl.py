from flask import *
from models.domain import Domain
from models.file_in_domain import FileInDomain
from library.auth_decorators import authenticate
from library.logic import for_domain
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



@domain_bp.route('/<domain_id>/files',
                 methods=['POST'])
@authenticate
def post_file_domain(user, domain_id):
     if request.method == 'POST':
        file = request.files['file']
        name = request.json.get('name')
        type_of_file = request.json.get('type_of_file')
        domain = Domain.objects(id=domain_id).first()
        if domain:
            dm = for_domain.add_file_to_domain(domain,
                                          file,
                                          name,
                                          'files',
                                          type_of_file)

            if dm:
                return 202
            else:
                return 403
        else:
            return "" , 404


@domain_bp.route('/<domain_id>/files/<file_id>',
                 methods=['PUT'])
@authenticate
def put_file_domain(user, domain_id, file_id):
    name = request.json.get('name')
    domain = Domain.objects(id=domain_id).first()
    if domain:
       fid = FileInDomain.objects(domain=domain.id,
                             id=file_id).first()
       if fid:
            fid.name = name
            res = fid.save_me()
            if 'errors' in res.keys():
                return jsonify(res), 403
            else:
                return jsonify(res)
       else:
           return "", 404
    else:
        return "", 404


@domain_bp.route('/<domain_id>', methods="PUT")
@authenticate
def put_domain_field(user, domain_id):
    domain_dict = request.json.get('domain')
    domain = Domain.objects(id=domain_id).first()
    if domain:
        for key in domain.keys():
            setattr(domain, key, domain[key])

        res = domain.save_me()
        if 'errors' in res.keys():
            return jsonify(res), 403
        else:
            return jsonify(res)
    else:
        return "", 404



