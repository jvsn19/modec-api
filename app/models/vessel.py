from ..utils import EquipmentID

class Vessel:
    def __init__(self, code: str) -> None:
        self._code = code
        self._equipments = []

    @property
    def code(self):
        return self._code
    
    @property
    def equipments(self) -> [EquipmentID]:
        return self._equipments

    def add_equipment(self, equipment_id: EquipmentID):
        self._equipments.append(equipment_id)