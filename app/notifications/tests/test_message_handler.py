import pytest
from app.notifications.models import Payload
from app.notifications.services.handler import MessageHandler


@pytest.mark.parametrize("types", ["whatsapp", "telegram", "push_notification"])
def test_message_handler(types):
    payload = Payload(type_platform=types, message="sdfsdf")
    response = MessageHandler(payload=payload).handle_message()
    assert response == f"{payload.message} - response"
