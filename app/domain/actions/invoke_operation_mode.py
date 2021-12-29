import inject

from app.domain.interfaces.abstract_database import AbstractDatabase
from app.domain.actions.change_device_status import ChangeDeviceStatus
from app.domain.operation_modes import Operation, AutoMode, AutoModeHeaterPriority


class InvokeOperationMode:
    @inject.autoparams()
    def __init__(self, db: AbstractDatabase):
        self._db = db
        self.change_device_status = ChangeDeviceStatus()

    def execute(self):
        operation = self._db.get_active_operation_mode()
        schedulers = self._db.get_low_cost_power_schedulers()
        temp_info = self._db.get_temp()

        new_statuses = []

        if operation == Operation.AUTO_MODE:
            check_schedule = self._db.get_checking_schedule_status(Operation.AUTO_MODE)
            mode = AutoMode(schedulers)
            new_statuses = mode.invoke(temp_info, check_schedule=check_schedule)
        elif operation == Operation.AUTO_MODE_HEATER:
            check_schedule = self._db.get_checking_schedule_status(Operation.AUTO_MODE_HEATER)
            mode = AutoModeHeaterPriority()
            new_statuses = mode.invoke(temp_info, check_schedule=check_schedule)

        self.change_device_status.run(new_statuses)
