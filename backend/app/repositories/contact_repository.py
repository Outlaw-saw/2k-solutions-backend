from typing import Any

from app.extensions import db
from app.models.contact_message import ContactMessage
from app.utils.helpers import apply_search, apply_sorting, paginate


class ContactRepository:
    def get_by_id(self, message_id: str) -> ContactMessage | None:
        return ContactMessage.query.filter_by(id=message_id).first()

    def list_paginated(self) -> dict[str, Any]:
        query = ContactMessage.query
        query = apply_search(query, ContactMessage, ["name", "email", "subject"])
        query = apply_sorting(query, ContactMessage)
        result = paginate(query)
        result["items"] = [m.to_dict() for m in result["items"]]
        return result

    def create(self, message: ContactMessage) -> ContactMessage:
        db.session.add(message)
        db.session.commit()
        return message

    def update(self, message: ContactMessage) -> ContactMessage:
        db.session.commit()
        return message
