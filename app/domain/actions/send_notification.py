import inject

from app.domain.devices import Devices
from app.domain.interfaces.abstract_notification_api import AbstractNotificationApi
from app.domain.interfaces.abstract_database import AbstractDatabase


messages = {
    Devices.WASHER.value: "💧 Pralka uprała",
    Devices.DRYER.value: "🐫 Suszarka skończyła pracę"
}


class SendNotification:
    @inject.autoparams()
    def __init__(self, api: AbstractNotificationApi, db: AbstractDatabase) -> None:
        self._api = api
        self._db = db
    
    def send_notification(self):
        devices = [Devices.WASHER.value, Devices.DRYER.value]
        for device_name in devices:
            washer_current_power = self._db.get_current_power(device_name)
            should_send_notification = self._db.get_notifier_status(device_name) and washer_current_power < 1

            if should_send_notification:
                chats = self._db.get_chats()
                self._api.send_notification(messages.get(device_name, "😵"), chats)
                self._db.set_notifier_status(device_name, False)
