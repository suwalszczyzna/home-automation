import inject

from app.domain.interfaces.abstract_database import AbstractDatabase


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
