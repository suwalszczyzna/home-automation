import inject

from app.domain.abstract_database import AbstractDatabase
from app.domain.actions.change_device_status import DeviceStatus
from app.domain.operation_modes import Operation, AutoMode, AutoModeHeaterPriority


class InvokeOperationMode:
    @inject.autoparams()
    def __init__(self, db: AbstractDatabase, device_status: DeviceStatus):
        self._db = db
        self._ds = device_status

    def execute(self):
        operation = self._db.get_active_operation_mode()
        schedulers = self._db.get_low_cost_power_schedulers()
        temp_info = self._db.get_temp()

        if operation == Operation.AUTO_MODE:
            mode = AutoMode(self._ds, schedulers)
            mode.invoke(temp_info, check_schedule=True)
        elif operation == Operation.AUTO_MODE_HEATER:
            mode = AutoModeHeaterPriority(self._ds)
            mode.invoke(temp_info)
