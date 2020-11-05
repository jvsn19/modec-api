import json

from ..utils import EquipmentStatus

class Equipment:
    def __init__(self, name: str, code: str, location: str) -> None:
        self._name = name
        self._code = code
        self._location = location
        self._status = EquipmentStatus.ACTIVE

    @property
    def status(self) -> str:
        return self._status

    @status.setter
    def status(self, new_status: EquipmentStatus) -> None:
        self._status = new_status

    @property
    def name(self) -> None:
        return self._name

    @property
    def code(self) -> None:
        return self._code

    @property
    def location(self) -> None:
        return self._location

    def to_dict(self):
        return {
            'name': self.name,
            'code': self.code,
            'location': self.location,
            'status': json.dumps(self.status),
        }