import uuid
from datetime import datetime, timezone

from app.extensions import db


class SiteSetting(db.Model):
    __tablename__ = "site_settings"

    id = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    brand_name = db.Column(db.String(100), nullable=False, default="2K Solutions")
    tagline = db.Column(db.String(200), nullable=True)
    address = db.Column(db.Text, nullable=True)
    phone = db.Column(db.String(20), nullable=True)
    email = db.Column(db.String(255), nullable=True)
    working_hours = db.Column(db.String(100), nullable=True)
    social_links = db.Column(db.JSON, nullable=True)
    copyright_year = db.Column(db.Integer, nullable=True)
    created_at = db.Column(db.DateTime(timezone=True), nullable=False, default=lambda: datetime.now(timezone.utc))
    updated_at = db.Column(db.DateTime(timezone=True), nullable=False, default=lambda: datetime.now(timezone.utc), onupdate=lambda: datetime.now(timezone.utc))

    def to_dict(self) -> dict:
        return {
            "id": str(self.id),
            "brand_name": self.brand_name,
            "tagline": self.tagline,
            "address": self.address,
            "phone": self.phone,
            "email": self.email,
            "working_hours": self.working_hours,
            "social_links": self.social_links,
            "copyright_year": self.copyright_year,
        }
