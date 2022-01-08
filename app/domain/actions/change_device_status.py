from typing import List

import inject

import logger
from app.domain.interfaces.abstract_database import AbstractDatabase
from app.domain.interfaces.abstract_device_api import AbstractDeviceAPI
from app.domain.devices import NewDeviceStatus

log = logger.get_logger("change-device-status")


class ChangeDeviceStatus:
    @inject.autoparams()
    def __init__(self, api: AbstractDeviceAPI, db: AbstractDatabase):
        self._api = api
        self._db = db

    def run(self, new_device_statuses: List[NewDeviceStatus]):
        for status in new_device_statuses:
            device = self._db.get_device_by_name(status.device.value)
            status_from_db = self._db.get_device_status(device.name)
            log.info("Status from db for device %s is %s", device.name, status_from_db)
            if status_from_db != status.status.value:
                log.info("Setting %s to %s using api", device.name, status.status)
                result = self._api.set_status(device, status.status)
                if result:
                    log.info("Saving new status to db (%s: %s)", device.name, status.status)
                    self._db.set_device_status(device.name, status.status)
            else:
                log.info("%s status is already %s (by db). Pass", device.name, status.status)
