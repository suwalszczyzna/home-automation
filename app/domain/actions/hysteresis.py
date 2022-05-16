import inject

from app.domain.devices import Hysteresis, Status
from app.domain.interfaces.abstract_database import AbstractDatabase


class HysteresisActions:
    @inject.autoparams()
    def __init__(self, db: AbstractDatabase):
        self.db = db

    def get_hysteresis(self) -> Hysteresis:
        return self.db.get_hysteresis()

    def update_hysteresis(self, status: bool, value: int) -> Hysteresis:
        self.db.set_hysteresis_status(Status(status))
        self.db.set_hysteresis_value(value)
        return self.db.get_hysteresis()
