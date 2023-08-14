from app.notifications.models import Payload
from app.logger import log


class MessengerInterface:
    def send(self, message: Payload) -> str:
        log.info(f"sending message {message} to WhatsApp|Push")
        return f"{message.message} - response"


class TelegramMessenger(MessengerInterface):
    def send(self, message: Payload) -> str:
        log.info(f"sending message {message} to Telegram")
        return f"{message.message} - response"
