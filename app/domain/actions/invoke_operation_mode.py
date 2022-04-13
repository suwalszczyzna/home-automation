import inject

import logger
from app.domain.interfaces.abstract_database import AbstractDatabase
from app.domain.actions.change_device_status import ChangeDeviceStatus
from app.domain.operation_modes import Operation, AutoMode, AutoModeHeaterPriority
from app.entrypoints.tasks.base import update_smart_device_status

log = logger.get_logger("InvokeOperationMode")


class InvokeOperationMode:
    @inject.autoparams()
    def __init__(self, db: AbstractDatabase):
        self._db = db
        self.change_device_status = ChangeDeviceStatus()

    def execute(self):
        operation = self._db.get_active_operation_mode()
        low_cost_schedules = self._db.get_low_cost_power_schedulers()
        temp_info = self._db.get_temp()

        new_statuses = []

        log.info("Operation mode: %s", operation)
        log.info("With temp: %s", temp_info.to_dict())

        if operation == Operation.AUTO_MODE:
            check_schedule = self._db.get_checking_schedule_status(Operation.AUTO_MODE)
            log.info("Operation mode: check schedule: %s", check_schedule)

            mode = AutoMode(low_cost_schedules)
            new_statuses = mode.invoke(temp_info, check_schedule=check_schedule)

        elif operation == Operation.AUTO_MODE_HEATER:
            check_schedule = self._db.get_checking_schedule_status(Operation.AUTO_MODE_HEATER)
            log.info("Check schedule: %s", check_schedule)

            mode = AutoModeHeaterPriority(low_cost_schedules)
            new_statuses = mode.invoke(temp_info, check_schedule=check_schedule)

        if new_statuses:
            self.change_device_status.run(new_statuses)

        update_smart_device_status.apply_async(countdown=5)
