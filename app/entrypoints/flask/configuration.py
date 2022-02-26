import os

import inject
from flask import Flask

import logger
from app.adapters.api.fake_api import FakeAPI
from app.adapters.database.fake_database import FakeDatabase
from app.adapters.sensors_api.fake_sensors_api import FakeSensorAPI
from app.domain.interfaces.abstract_database import AbstractDatabase
from app.domain.interfaces.abstract_device_api import AbstractDeviceAPI
from app.domain.interfaces.abstract_sensor_api import AbstractSensorApi

log = logger.get_logger("configuration")


def is_production(prod_env: str):
    if prod_env == 'true':
        log.info("Production mode")
        return True
    else:
        log.info("Debug mode")
        return False


def get_smart_device_api(prod_env: str):
    if is_production(prod_env):
        from app.adapters.api.tuya_api import TuyaAPI
        return TuyaAPI()
    else:
        return FakeAPI()


def get_sensor_api(prod_env: str):
    if is_production(prod_env):
        from app.adapters.sensors_api.sensors_api import SensorsAPI
        return SensorsAPI()
    else:
        return FakeSensorAPI()


def get_db(prod_env: str, uri: str):
    if is_production(prod_env):
        from app.adapters.database.postgres_database import PostgresDB
        return PostgresDB(uri)
    else:
        return FakeDatabase(uri)


def configure_application(application: Flask) -> None:
    application.config.update(
        DATABASE_URI=os.getenv('DATABASE_URI')
    )
    application.config.update(
        PROD=os.getenv('PROD')
    )


def configure_inject(application: Flask) -> None:
    def config(binder: inject.Binder) -> None:
        binder.bind(AbstractDatabase, get_db(application.config['PROD'], application.config['DATABASE_URI']))
        binder.bind(AbstractDeviceAPI, get_smart_device_api(application.config['PROD']))
        binder.bind(AbstractSensorApi, get_sensor_api(application.config['PROD']))

    inject.configure(config)
