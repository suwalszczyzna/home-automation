import inject

import logger
from app.domain.interfaces.abstract_sensor_api import AbstractSensorApi
from app.domain.interfaces.abstract_database import AbstractDatabase

log = logger.get_logger("SaveTempsensorsValues")


class SaveTempsensorsValues:
    @inject.autoparams()
    def __init__(self, api: AbstractSensorApi, db: AbstractDatabase):
        self._api = api
        self._db = db

    def run(self):
        sensors = self._api.get_all_sensors()
        log.info("Got %s sensors", len(sensors))
        for sensor in sensors:
            log.info("Updating sensor: %s", sensor.__repr__())
            self._db.save_temp(sensor)
