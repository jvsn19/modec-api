import pytest

from app import create_app
from app.db import CustomDatabase

@pytest.fixture
def app():
    return create_app().test_client()

@pytest.fixture
def db():
    class DatabaseHandler:
        database = CustomDatabase

        @classmethod
        def reset_db(cls):
            cls.database._vessels.clear()
            cls.database._equipments.clear()

        @classmethod
        def create_vessel(cls, vessel_id):
            cls.database.add_vessel(vessel_id)

        @classmethod
        def create_equipment(cls, vessel_id, equipment_id, name, location):
            cls.database.add_equipment(vessel_id, equipment_id, name, location)
        
    return DatabaseHandler()

@pytest.fixture
def app_helper(app):
    class Helper:
        flask_client = app

        @classmethod
        def create_vessel(cls, vessel_id):
            body = {
                'vessel-id': vessel_id,
            }

            return cls.flask_client.post('/register-vessel', json=body)

        @classmethod
        def create_equipment(cls, vessel_id, equipment_id, name, location):
            body = {
                "vessel-id": vessel_id,
                "equipment-id": equipment_id,
                "location": location,
                "name": name
            }

            return cls.flask_client.post('/register-equipment', json=body)

        @classmethod
        def update_equipment(cls, equipment_id, status):
            body = {
                'equipment-id': equipment_id,
                'status': status
            }

            return cls.flask_client.patch('/update-equipment', json=body)

        @classmethod
        def get_equipments(cls, vessel_id):
            return cls.flask_client.get(f'get-equipments?vessel-id={vessel_id}')

    return Helper()