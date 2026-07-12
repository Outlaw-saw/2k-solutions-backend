import uuid
from datetime import datetime, timezone

from app.extensions import db


class Differentiator(db.Model):
    __tablename__ = "differentiators"

    id = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    number = db.Column(db.Integer, nullable=False)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=True)
    icon_class = db.Column(db.String(50), nullable=True)
    display_order = db.Column(db.Integer, nullable=False, default=0)
    created_at = db.Column(db.DateTime(timezone=True), nullable=False, default=lambda: datetime.now(timezone.utc))

    def to_dict(self) -> dict:
        return {
            "id": str(self.id),
            "number": self.number,
            "title": self.title,
            "description": self.description,
            "icon_class": self.icon_class,
            "display_order": self.display_order,
        }
