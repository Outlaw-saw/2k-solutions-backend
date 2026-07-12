import uuid
from datetime import datetime, timezone

from app.extensions import db


class Testimonial(db.Model):
    __tablename__ = "testimonials"

    id = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    student_name = db.Column(db.String(100), nullable=False)
    initials = db.Column(db.String(4), nullable=True)
    role = db.Column(db.String(100), nullable=True)
    quote = db.Column(db.Text, nullable=False)
    rating = db.Column(db.Integer, nullable=False, default=5)
    display_order = db.Column(db.Integer, nullable=False, default=0)
    is_active = db.Column(db.Boolean, nullable=False, default=True)
    created_at = db.Column(db.DateTime(timezone=True), nullable=False, default=lambda: datetime.now(timezone.utc))

    def to_dict(self) -> dict:
        return {
            "id": str(self.id),
            "student_name": self.student_name,
            "initials": self.initials,
            "role": self.role,
            "quote": self.quote,
            "rating": self.rating,
            "display_order": self.display_order,
        }
