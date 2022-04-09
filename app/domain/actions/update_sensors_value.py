import inject

import logger
from app.domain.devices import Devices, POWER_DEVICES
from app.domain.interfaces.abstract_sensor_api import AbstractSensorApi
from app.domain.interfaces.abstract_device_api import AbstractDeviceAPI
from app.domain.interfaces.abstract_database import AbstractDatabase
from app.domain.actions.smart_device_statuses import SmartDevicesStatuses

log = logger.get_logger("UpdateSensorsValues")


class UpdateSensorsValue:
    @inject.autoparams()
    def __init__(self, sensor_api: AbstractSensorApi, db: AbstractDatabase, device_api:AbstractDeviceAPI ):
        self._sensor_api = sensor_api
        self._db = db
        self._device_api = device_api

    def update_temp(self):
        sensors = self._sensor_api.get_all_temp_sensors()
        log.info("Got %s sensors", len(sensors))
        for sensor in sensors:
            log.info("Updating sensor: %s", sensor.__repr__())
            self._db.save_temp(sensor)

    def update_current_power(self):
        for device_name in POWER_DEVICES:
            log.info("Update current power for device: %s", device_name)
            device = self._db.get_device_by_name(device_name)
            current_device_power = self._device_api.get_current_power(device)
            self._db.set_current_power(device.name, current_device_power)
            if current_device_power > 1:
                self._db.set_notifier_status(device_name, True)
