import os

import inject
from flask import Flask

from app.adapters.api.fake_api import FakeAPI
from app.adapters.database.postgres_database import PostgresDB
from app.domain.abstract_database import AbstractDatabase
from app.domain.abstract_device_api import AbstractDeviceAPI


def configure_application(application: Flask) -> None:
    application.config.update(
        DATABASE_URI=os.getenv('DATABASE_URI')
    )


def configure_inject(application: Flask) -> None:
    def config(binder: inject.Binder) -> None:
        binder.bind(AbstractDatabase, PostgresDB(application.config['DATABASE_URI']))
        binder.bind(AbstractDeviceAPI, FakeAPI())

    inject.configure(config)
