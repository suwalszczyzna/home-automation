import inject

import logger
from app.domain.devices import Devices
from app.domain.interfaces.abstract_sensor_api import AbstractSensorApi
from app.domain.interfaces.abstract_device_api import AbstractDeviceAPI
from app.domain.interfaces.abstract_database import AbstractDatabase

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
        log.info("Update current power")
        washer = self._db.get_device_by_name(Devices.WASHER.value)
        washer_current_power = self._device_api.get_current_power(washer)
        self._db.set_current_power(washer.name, washer_current_power)
