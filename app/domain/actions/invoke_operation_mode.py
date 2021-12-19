import inject

from app.domain.abstract_database import AbstractDatabase
from app.domain.operation_modes import Operation, AutoMode


class InvokeOperationMode:
    @inject.autoparams()
    def __init__(self, db: AbstractDatabase):
        self._db = db

    def execute(self):
        operation = self._db.get_active_operation_mode()
        schedulers = self._db.get_low_cost_power_schedulers()

        if operation == Operation.AUTO_MODE:
            mode = AutoMode(schedulers)
            temp_info = self._db.get_temp()
            mode.invoke(temp_info, check_schedule=True)
