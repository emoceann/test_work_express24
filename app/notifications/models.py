from pydantic import BaseModel
from enum import Enum


class Platforms(Enum):
    whatsapp = "whatsapp"
    telegram = "telegram"
    push_notification = "push_notification"


class Payload(BaseModel):
    type_platform: Platforms
    message: str
