from flask import Blueprint

# name, file(location reference), url_prefix
bp = Blueprint('api', __name__, url_prefix='/')

from .import routes # AKA use routes from the same folder
