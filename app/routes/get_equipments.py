from flask import request

from . import routes
from ..db import CustomDatabase
from ..utils import VesselDoesNotExistException

@routes.route('/get-equipments', methods=['GET'])
def get_equipments() -> None:
    vessel_id = request.args.get('vessel-id')
    try:
        equipments_json = CustomDatabase.get_all_equipments(vessel_id)
        return equipments_json , 200
    except VesselDoesNotExistException as ex:
        return str(ex), 404
    except Exception as ex:
        return 'Bad Request', 400