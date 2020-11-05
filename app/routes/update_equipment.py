from flask import request

from . import routes
from ..db import CustomDatabase
from ..utils import EquipmentDoesNotExistException, InvalidStatusException

@routes.route('/update-equipment', methods=['PATCH'])
def update_equipment() -> None:
    response_json = request.get_json()
    params = {
        'equipment_id': response_json['equipment-id'],
        'status': response_json['status']
    }
    try:
        CustomDatabase.update_equipment(**params)
        return "OK", 200
    except EquipmentDoesNotExistException as ex:
        return str(ex), 404
    except InvalidStatusException as ex:
        return str(ex), 406
    except Exception as _:
        return "Bad Request", 400