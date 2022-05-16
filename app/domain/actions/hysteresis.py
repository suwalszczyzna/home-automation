import inject

from app.domain.interfaces.abstract_database import AbstractDatabase


class HysteresisActions:
    @inject.autoparams()
    def __init__(self, db: AbstractDatabase):
        self.db = db

    def get_hysteresis(self):
        return {
            "value": self.db.get_hysteresis_value(),
            "status": self.db.get_hysteresis_status()
        }

    def update_hysteresis(self, status: bool, value: int):
        self.db.set_hysteresis_status(status)
        self.db.update_hysteresis_value(value)
        return {
            "code": "ok"
        }