from app.notifications.models import Payload
from app.notifications.services.senders import MessengerInterface, TelegramMessenger
from app.logger import log


class MessageHandler:
    def __init__(self, payload: Payload):
        self.payload = payload

    def handle_message(self):
        log.info(f"received {self.payload=} to handle")
        if self.payload.type_platform.name in ["whatsapp", "push_notification"]:
            response = MessengerInterface().send(self.payload)
        else:
            response = TelegramMessenger().send(self.payload)
        log.info(f"{response}")
        return response
