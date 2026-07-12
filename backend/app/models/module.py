import uuid
from datetime import datetime, timezone

from app.extensions import db


class Module(db.Model):
    __tablename__ = "modules"

    id = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    course_id = db.Column(db.String(36), db.ForeignKey("courses.id", ondelete="CASCADE"), nullable=False, index=True)
    title = db.Column(db.String(150), nullable=False)
    description = db.Column(db.Text, nullable=True)
    icon_class = db.Column(db.String(50), nullable=True)
    display_order = db.Column(db.Integer, nullable=False, default=0)
    created_at = db.Column(db.DateTime(timezone=True), nullable=False, default=lambda: datetime.now(timezone.utc))

    course = db.relationship("Course", back_populates="modules")

    def to_dict(self) -> dict:
        return {
            "id": str(self.id),
            "course_id": str(self.course_id),
            "title": self.title,
            "description": self.description,
            "icon_class": self.icon_class,
            "display_order": self.display_order,
        }
