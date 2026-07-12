import uuid
from datetime import datetime, timezone

from app.extensions import db


class Technology(db.Model):
    __tablename__ = "technologies"

    id = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    name = db.Column(db.String(50), nullable=False)
    icon_class = db.Column(db.String(50), nullable=True)
    display_order = db.Column(db.Integer, nullable=False, default=0)
    created_at = db.Column(db.DateTime(timezone=True), nullable=False, default=lambda: datetime.now(timezone.utc))

    def to_dict(self) -> dict:
        return {
            "id": str(self.id),
            "name": self.name,
            "icon_class": self.icon_class,
            "display_order": self.display_order,
        }
