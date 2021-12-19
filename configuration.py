import os

import inject
from flask import Flask

from app.adapters.database.fake_database import FakeDatabase
from app.domain.abstract_database import AbstractDatabase


def configure_application(application: Flask) -> None:
    application.config.update(
        # DATABASE_URI=os.getenv('DATABASE_URI')
        DATABASE_URI="SOME_FAKE_DB_URI"
    )


def configure_inject(application: Flask) -> None:
    def config(binder: inject.Binder) -> None:
        binder.bind(AbstractDatabase, FakeDatabase(application.config['DATABASE_URI']))

    inject.configure(config)
