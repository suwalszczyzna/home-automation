from dataclasses import dataclass


sensors_desc = {
    "0119523a78ff": {"name": "raw_sensor", "temp_calibration_value": 0},
    "00000d9931fa": {"name": "sensor_co", "temp_calibration_value": 0},
    "00000d96c007": {"name": "sensor_water", "temp_calibration_value": 10}
}


class TempSensor:
    def __init__(self, sensor_id: str, value: float):
        self.sensor_id = sensor_id
        self.raw_value = value
        self._sensor_config = sensors_desc.get(sensor_id)

    @property
    def name(self):
        return self._sensor_config.get("name", self.sensor_id)

    @property
    def temperature(self):
        temp = self.raw_value + self._sensor_config.get("temp_calibration_value")
        return round(temp)

    def __repr__(self):
        return f"<TempSensor name={self.name} temperature={self.temperature}>"
