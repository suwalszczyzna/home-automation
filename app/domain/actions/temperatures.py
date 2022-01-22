import os
from datetime import datetime, timedelta

import inject

import logger
from app.domain.interfaces.abstract_database import AbstractDatabase

log = logger.get_logger("TemperaturesActions")


class Temperatures:
    @inject.autoparams()
    def __init__(self, db: AbstractDatabase):
        self._db = db

    def get_actual_temperatures(self):
        temp = self._db.get_temp()
        return {
            "co_temp": temp.co_temp,
            "water_temp": temp.water_temp,
        }

    def clean_temp_history(self):
        max_history = datetime.now() - timedelta(int(os.getenv('READ_SENSORS_INTERVAL')))
        log.info("Cleaning temp history")
        self._db.clean_temp_history(max_history)
