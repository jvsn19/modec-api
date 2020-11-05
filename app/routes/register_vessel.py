from flask import request

from . import routes
from ..db import CustomDatabase
from ..utils import VesselAlreadyCreatedException

@routes.route('/register-vessel', methods=['POST'])
def register_vessel() -> None:
    response_json = request.get_json()
    try:
        CustomDatabase.add_vessel(vessel_id = response_json['vessel-id'])
        return "Created", 201
    except VesselAlreadyCreatedException as ex:
        return str(ex), 409
    except Exception as _:
        return "Bad Request", 400