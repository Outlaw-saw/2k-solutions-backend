import uuid
from datetime import datetime, timezone

from app.extensions import db


class Milestone(db.Model):
    __tablename__ = "milestones"

    id = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    label = db.Column(db.String(100), nullable=False)
    value = db.Column(db.Integer, nullable=False)
    icon_class = db.Column(db.String(50), nullable=True)
    section = db.Column(db.String(20), nullable=False, default="milestones")
    display_order = db.Column(db.Integer, nullable=False, default=0)
    created_at = db.Column(db.DateTime(timezone=True), nullable=False, default=lambda: datetime.now(timezone.utc))

    def to_dict(self) -> dict:
        return {
            "id": str(self.id),
            "label": self.label,
            "value": self.value,
            "icon_class": self.icon_class,
            "section": self.section,
            "display_order": self.display_order,
        }
