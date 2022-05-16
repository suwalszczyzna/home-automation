import inject

from app.domain.interfaces.abstract_database import AbstractDatabase
from app.domain.operation_modes import Operation


class ManageOperationModes:
    @inject.autoparams()
    def __init__(self, db: AbstractDatabase):
        self._db = db

    def get_active_operation_mode(self):
        operation = self._db.get_active_operation_mode()
        heater_mode = self._db.get_checking_schedule_status(operation)

        return {
            "operation_mode": operation.value,
            "heater_on_lower_cost_only": heater_mode
        }
    
    def set_active_operation_mode(self, operation: str):
        self._db.set_active_operation_mode(Operation(operation))

        return {
            "code": "ok"
        }
    
    def set_checking_low_cost(self, operation: str, should_check: bool):
        self._db.set_low_cost_checking(Operation(operation), should_check)
        
        return {
            "code": "ok"
        }