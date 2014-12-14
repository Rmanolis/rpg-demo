from models.domain import Domain
from models.file_in_domain import FileInDomain
from werkzeug import secure_filename
import os
from flask import *
import settings

def add_domain(user, name):
    dom = Domain()
    dom.user = user.to_dbref()
    dom.name = name
    return dom.save_me()

def get_extension(filename):
    splitted = filename.rsplit('.', 1)
    if len(splitted) == 2:
        return splitted[1]
    else:
        return None

def allowed_file(filename):
    return '.' in filename and \
           get_extension(filename) in settings.ALLOWED_EXTENSIONS

def add_file_to_domain(domain, file  , name,
                       folder, type_of_file):
     fid = FileInDomain().save()
     fid.domain=domain.to_dbref()
     fid.name = name
     fid.type_of_file = type_of_file
     if file and allowed_file(file.filename):
        fid.extension = get_extension(file.filename)
        if not fid.extension:
            return "This is not a correct file with a proper extension"
        if fid.extension not in settings.EXTENSIONS_BY_ENUM[type_of_file]:
            fid.delete()
            return "The extension is not correct"
        fid.filename = str(fid.id) + "." + fid.extension
        filename = secure_filename(fid.filename)
        file.save(os.path.join(folder, filename))
        fid.save()
        return None
     else:
        fid.delete()
        return "The file is not allowed"


