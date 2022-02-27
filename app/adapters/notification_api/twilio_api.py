import logger

from typing import List
from twilio.rest import Client
from twilio.base.exceptions import TwilioRestException

from app.domain.interfaces.abstract_notification_api import AbstractNotificationApi
from app.domain.notification import Subscriber

log = logger.get_logger("PostgresDB")


class TwilioApi(AbstractNotificationApi):
    def __init__(self, sid, token) -> None:
        self.client = Client(sid, token)

    def send_notification(self, receivers: List[Subscriber], message: str):
        try:
            for subscriber in receivers:
                message = self.client.messages.create(
                    to=f"whatsapp:+48{subscriber.number}",
                    from_="whatsapp:+14155238886",
                    body=message,)

                log.info(f"Message for: {subscriber.number}, SID: {message.sid}")

        except TwilioRestException as e:
            log.error("Twilio has a problem", exc_info=e)
