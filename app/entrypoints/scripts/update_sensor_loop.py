from time import sleep

import requests

import logger

log = logger.get_logger("update-sensor-loop")


def run_update_sensor():
    requests.get("http://127.0.0.1:5000/api/update_sensors_values")


if __name__ == '__main__':
    while True:
        try:
            run_update_sensor()
        except:
            pass
        sleep(10)
