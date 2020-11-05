from flask import Blueprint

routes = Blueprint('__routes__', __name__)

from .register_vessel import *
from .register_equipment import *
from .get_equipments import *
from .update_equipment import *