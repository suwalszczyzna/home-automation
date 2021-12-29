import inject

import logger
from app.domain.interfaces.abstract_sensor_api import AbstractSensorApi
from app.domain.interfaces.abstract_database import AbstractDatabase

log = logger.get_logger("SaveTempsensorsValues")


class SaveTempsensorsValues:
    @inject.autoparams()
    def __init__(self, sensor_api: AbstractSensorApi, db: AbstractDatabase):
        self._sensor_api = sensor_api
        self._db = db

    def run(self):
        sensors = self._sensor_api.get_all_sensors()
        log.info("Got %s sensors", len(sensors))
        for sensor in sensors:
            log.info("Updating sensor: %s", sensor.__repr__())
            self._db.save_temp(sensor)
