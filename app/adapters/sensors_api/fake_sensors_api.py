import random
from typing import List

import logger
from app.domain.interfaces.abstract_sensor_api import AbstractSensorApi
from app.domain.sensors import TempSensor

log = logger.get_logger("FakeSensorAPI")


class FakeSensorAPI(AbstractSensorApi):
    def get_all_sensors(self) -> List[TempSensor]:
        log.info("Data from FakeSensorAPI")
        return[
            TempSensor("00000d9931fa", random.randint(30, 50)),
            TempSensor("00000d96c007", random.randint(14, 39)),
            TempSensor("0119523a78ff", random.randint(19, 24)),
        ]
