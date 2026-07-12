import uuid
from datetime import datetime, timezone

from app.extensions import db


class Course(db.Model):
    __tablename__ = "courses"

    id = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    slug = db.Column(db.String(50), unique=True, nullable=False, index=True)
    title = db.Column(db.String(100), nullable=False)
    subtitle = db.Column(db.String(200), nullable=True)
    description = db.Column(db.Text, nullable=True)
    definition = db.Column(db.Text, nullable=True)
    quote = db.Column(db.Text, nullable=True)
    duration_months = db.Column(db.Integer, nullable=False)
    num_projects = db.Column(db.Integer, nullable=False, default=0)
    badge = db.Column(db.String(50), nullable=True)
    icon_class = db.Column(db.String(50), nullable=True)
    curriculum = db.Column(db.JSON, nullable=True)
    career_outcomes = db.Column(db.JSON, nullable=True)
    history = db.Column(db.Text, nullable=True)
    is_active = db.Column(db.Boolean, nullable=False, default=True)
    display_order = db.Column(db.Integer, nullable=False, default=0)
    created_at = db.Column(db.DateTime(timezone=True), nullable=False, default=lambda: datetime.now(timezone.utc))
    updated_at = db.Column(db.DateTime(timezone=True), nullable=False, default=lambda: datetime.now(timezone.utc), onupdate=lambda: datetime.now(timezone.utc))

    modules = db.relationship("Module", back_populates="course", lazy="dynamic", cascade="all, delete-orphan")
    enrollments = db.relationship("Enrollment", back_populates="course", lazy="dynamic")

    def to_dict(self) -> dict:
        return {
            "id": str(self.id),
            "slug": self.slug,
            "title": self.title,
            "subtitle": self.subtitle,
            "description": self.description,
            "definition": self.definition,
            "quote": self.quote,
            "duration_months": self.duration_months,
            "num_projects": self.num_projects,
            "badge": self.badge,
            "icon_class": self.icon_class,
            "curriculum": self.curriculum,
            "career_outcomes": self.career_outcomes,
            "history": self.history,
            "is_active": self.is_active,
            "display_order": self.display_order,
            "created_at": self.created_at.isoformat() if self.created_at else None,
        }
