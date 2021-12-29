from time import sleep

import requests
from requests import ReadTimeout

import logger

log = logger.get_logger("update-sensor-loop")


def run_update_sensor():
    try:
        requests.get("http://127.0.0.1:5000/api/update_sensors_values", timeout=5)
    except Exception as e:
        log.error("Error", exc_info=e)


if __name__ == '__main__':
    while True:
        run_update_sensor()
        sleep(10)
