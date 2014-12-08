from models.domain import Domain
from flask import *
import settings

def add_domain(user, name):
    dom = Domain()
    dom.user = user.to_dbref()
    dom.name = name
    return dom.save_me()

def get_extension(filename):
    return filename.rsplit('.', 1)[1]

def allowed_file(filename):
    return '.' in filename and \
           get_extension(filename) in settings.ALLOWED_EXTENSIONS

def add_file_to_domain(domain, file  , name,
                       folder, type_of_file):
     fid = FileInDomain().save()
     fid.filename = str(sid.id)
     fid.name = str(sid.id)
     fid.type_of_file = type_of_file
     if file and allowed_file(file.filename):
        fid.extension = get_extension(file.filename)
        filename = secure_filename(sid.filename)
        file.save(os.path.join(folder, filename))
        fid.save()
        return True
     else:
        return False

