import os

import inject
from flask import Flask

from app.adapters.api.fake_api import FakeAPI
from app.adapters.database.postgres_database import PostgresDB
from app.adapters.sensors_api.sensors_api import SensorsAPI
from app.domain.interfaces.abstract_database import AbstractDatabase
from app.domain.interfaces.abstract_device_api import AbstractDeviceAPI
from app.domain.interfaces.abstract_sensor_api import AbstractSensorApi


def configure_application(application: Flask) -> None:
    application.config.update(
        DATABASE_URI=os.getenv('DATABASE_URI')
    )


def configure_inject(application: Flask) -> None:
    def config(binder: inject.Binder) -> None:
        binder.bind(AbstractDatabase, PostgresDB(application.config['DATABASE_URI']))
        binder.bind(AbstractDeviceAPI, FakeAPI())
        binder.bind(AbstractSensorApi, SensorsAPI())

    inject.configure(config)
