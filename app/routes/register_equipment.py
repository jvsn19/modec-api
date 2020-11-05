from flask import request

from . import routes
from ..db import CustomDatabase
from ..utils import VesselDoesNotExistException, EquipmentAlreadyCreatedException

@routes.route('/register-equipment', methods=['POST'])
def register_equipment() -> None:
    response_json = request.get_json()
    params = {
        'vessel_id': response_json['vessel-id'],
        'equipment_id': response_json['equipment-id'],
        'name': response_json['name'],
        'location': response_json['location'],
    }
    try:
        CustomDatabase.add_equipment(**params)
        return "Created", 201
    except EquipmentAlreadyCreatedException as ex:
        return str(ex), 409
    except VesselDoesNotExistException as ex:
        return str(ex), 404
    except Exception as _:
        return "Bad Request", 400