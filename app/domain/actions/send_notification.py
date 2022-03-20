import inject

from app.domain.devices import Devices
from app.domain.interfaces.abstract_notification_api import AbstractNotificationApi
from app.domain.interfaces.abstract_database import AbstractDatabase


class SendNotification:
    @inject.autoparams()
    def __init__(self, api: AbstractNotificationApi, db: AbstractDatabase) -> None:
        self._api = api
        self._db = db
    
    def send_notification(self):
        device_name = Devices.WASHER.value
        should_send_notification = self._db.get_notifier_status(device_name)
        washer_current_power = self._db.get_current_power(device_name)
        if should_send_notification and washer_current_power < 1:
            self._api.send_notification("Pralka uprała 👍")
            self._db.set_notifier_status(device_name, False)
