import inject

from app.domain.interfaces.abstract_database import AbstractDatabase


class GetSensorsValue:
    @inject.autoparams()
    def __init__(self, db: AbstractDatabase):
        self._db = db

    def get_actual_temperatures(self):
        temp = self._db.get_temp()
        return {
            "co_temp": temp.co_temp,
            "water_temp": temp.water_temp,
        }
