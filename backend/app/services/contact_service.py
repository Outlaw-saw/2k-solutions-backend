from typing import Any

from app.models.contact_message import ContactMessage
from app.repositories.contact_repository import ContactRepository
from app.schemas.contact import ContactCreateSchema
from app.utils.errors import NotFoundError


class ContactService:
    def __init__(self) -> None:
        self.repo = ContactRepository()

    def create(self, data: dict[str, Any]) -> ContactMessage:
        schema = ContactCreateSchema()
        validated = schema.load(data)
        message = ContactMessage(**validated)
        return self.repo.create(message)

    def list_paginated(self) -> dict[str, Any]:
        return self.repo.list_paginated()

    def mark_as_read(self, message_id: str) -> ContactMessage:
        message = self.repo.get_by_id(message_id)
        if not message:
            raise NotFoundError("Message not found")
        message.is_read = True
        return self.repo.update(message)
