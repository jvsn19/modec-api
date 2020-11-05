from ..utils import *
from ..models import *

class Singleton(type):
    _instance = None
    
    def __call__(cls):
        if cls._instance is None:
            cls._instance = super().__call__()
        
        return cls._instance

class CustomDatabase(metaclass = Singleton):
    _vessels = {}
    _equipments = {}

    @classmethod
    def add_vessel(cls, vessel_id: VesselID) -> None:
        if cls._vessels.get(vessel_id) is not None:
            raise VesselAlreadyCreatedException(vessel_id)

        new_vessel = Vessel(vessel_id)
        cls._vessels[vessel_id] = new_vessel

    @classmethod
    def add_equipment(
        cls, 
        vessel_id: VesselID, 
        equipment_id: EquipmentID, 
        name: str, 
        location: str
    ) -> None:
        if cls._vessels.get(vessel_id) is None:
            raise VesselDoesNotExistException(vessel_id)

        if cls._equipments.get(equipment_id) is not None:
            raise EquipmentAlreadyCreatedException(equipment_id)

        cls._equipments[equipment_id] = Equipment(name, equipment_id, location)
        cls._vessels[vessel_id].add_equipment(equipment_id)

    @classmethod
    def get_all_equipments(cls, vessel_id: VesselID) -> [Equipment]:
        if cls._vessels.get(vessel_id) is None:
            raise VesselDoesNotExistException(vessel_id)

        equipments = cls._vessels[vessel_id].equipments
        to_return = {}

        for equipment in equipments:
            to_return[equipment] = cls._equipments[equipment].to_dict()

        return to_return

    @classmethod
    def update_equipment(cls, equipment_id: EquipmentID, status: EquipmentStatus) -> None:
        if status not in [EquipmentStatus.ACTIVE, EquipmentStatus.INACTIVE]:
            raise InvalidStatusException(status)
            
        if cls._equipments.get(equipment_id) is None:
            raise EquipmentDoesNotExistException(equipment_id)

        cls._equipments[equipment_id].status = status