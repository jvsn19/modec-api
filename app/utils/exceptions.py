class VesselAlreadyCreatedException(Exception):
    def __init__(self, vessel_id: str) -> None:
        super().__init__(f'The vessel {vessel_id} already exists')

class VesselDoesNotExistException(Exception):
    def __init__(self, vessel_id: str) -> None:
        super().__init__(f'The vessel {vessel_id} doesn\'t exist')

class EquipmentAlreadyCreatedException(Exception):
    def __init__(self, equipment_id: str) -> None:
        super().__init__(f'The equipment {equipment_id} already exists')

class EquipmentDoesNotExistException(Exception):
    def __init__(self, equipment_id: str) -> None:
        super().__init__(f'The equipment {equipment_id} does not exist')

class InvalidStatusException(Exception):
    def __init__(self, status) -> None:
        super().__init__(f'Invalid status {status}')