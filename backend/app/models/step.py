import uuid
from datetime import datetime, timezone

from app.extensions import db


class Step(db.Model):
    __tablename__ = "steps"

    id = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    step_number = db.Column(db.Integer, nullable=False)
    title = db.Column(db.String(200), nullable=False)
    description = db.Column(db.Text, nullable=True)
    icon_class = db.Column(db.String(50), nullable=True)
    created_at = db.Column(db.DateTime(timezone=True), nullable=False, default=lambda: datetime.now(timezone.utc))

    def to_dict(self) -> dict:
        return {
            "id": str(self.id),
            "step_number": self.step_number,
            "title": self.title,
            "description": self.description,
            "icon_class": self.icon_class,
        }
