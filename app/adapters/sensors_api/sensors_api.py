from typing import List

from w1thermsensor import W1ThermSensor

import logger
from app.domain.interfaces.abstract_sensor_api import AbstractSensorApi
from app.domain.sensors import TempSensor

log = logger.get_logger("SensorsAPI")


class SensorsAPI(AbstractSensorApi):
    def get_all_sensors(self) -> List[TempSensor]:
        result = []
        available_sensors = W1ThermSensor.get_available_sensors()

        log.info("Available %s sensors", len(available_sensors))

        for w1_sensor in available_sensors:
            result.append(
                TempSensor(
                    sensor_id=w1_sensor.id,
                    value=w1_sensor.get_temperature()
                )
            )

        return result
