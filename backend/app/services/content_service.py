from typing import Any

from app.models.service import Service
from app.models.testimonial import Testimonial
from app.models.faq import FAQ
from app.models.technology import Technology
from app.models.milestone import Milestone
from app.models.step import Step
from app.models.differentiator import Differentiator
from app.models.site_setting import SiteSetting
from app.repositories.content_repository import ContentRepository
from app.schemas.content import (
    ServiceSchema, TestimonialSchema, FAQSchema, TechnologySchema,
    MilestoneSchema, StepSchema, DifferentiatorSchema, SiteSettingSchema,
)
from app.utils.errors import NotFoundError


class ContentService:
    def __init__(self) -> None:
        self.repo = ContentRepository()

    # Services
    def list_services(self) -> list[dict[str, Any]]:
        return [s.to_dict() for s in self.repo.list_services()]

    def create_service(self, data: dict[str, Any]) -> Service:
        schema = ServiceSchema()
        validated = schema.load(data)
        service = Service(**validated)
        return self.repo.create_service(service)

    def update_service(self, service_id: str, data: dict[str, Any]) -> Service:
        service = self.repo.get_service(service_id)
        if not service:
            raise NotFoundError("Service not found")
        schema = ServiceSchema()
        validated = schema.load(data, partial=True)
        for key, value in validated.items():
            setattr(service, key, value)
        return self.repo.update_service(service)

    def delete_service(self, service_id: str) -> None:
        service = self.repo.get_service(service_id)
        if not service:
            raise NotFoundError("Service not found")
        self.repo.delete_service(service)

    # Testimonials
    def list_testimonials(self) -> list[dict[str, Any]]:
        return [t.to_dict() for t in self.repo.list_testimonials()]

    def create_testimonial(self, data: dict[str, Any]) -> Testimonial:
        schema = TestimonialSchema()
        validated = schema.load(data)
        testimonial = Testimonial(**validated)
        return self.repo.create_testimonial(testimonial)

    def update_testimonial(self, testimonial_id: str, data: dict[str, Any]) -> Testimonial:
        testimonial = self.repo.get_testimonial(testimonial_id)
        if not testimonial:
            raise NotFoundError("Testimonial not found")
        schema = TestimonialSchema()
        validated = schema.load(data, partial=True)
        for key, value in validated.items():
            setattr(testimonial, key, value)
        return self.repo.update_testimonial(testimonial)

    def delete_testimonial(self, testimonial_id: str) -> None:
        testimonial = self.repo.get_testimonial(testimonial_id)
        if not testimonial:
            raise NotFoundError("Testimonial not found")
        self.repo.delete_testimonial(testimonial)

    # FAQs
    def list_faqs(self) -> list[dict[str, Any]]:
        return [f.to_dict() for f in self.repo.list_faqs()]

    def create_faq(self, data: dict[str, Any]) -> FAQ:
        schema = FAQSchema()
        validated = schema.load(data)
        faq = FAQ(**validated)
        return self.repo.create_faq(faq)

    def update_faq(self, faq_id: str, data: dict[str, Any]) -> FAQ:
        faq = self.repo.get_faq(faq_id)
        if not faq:
            raise NotFoundError("FAQ not found")
        schema = FAQSchema()
        validated = schema.load(data, partial=True)
        for key, value in validated.items():
            setattr(faq, key, value)
        return self.repo.update_faq(faq)

    def delete_faq(self, faq_id: str) -> None:
        faq = self.repo.get_faq(faq_id)
        if not faq:
            raise NotFoundError("FAQ not found")
        self.repo.delete_faq(faq)

    # Technologies
    def list_technologies(self) -> list[dict[str, Any]]:
        return [t.to_dict() for t in self.repo.list_technologies()]

    def create_technology(self, data: dict[str, Any]) -> Technology:
        schema = TechnologySchema()
        validated = schema.load(data)
        tech = Technology(**validated)
        return self.repo.create_technology(tech)

    def delete_technology(self, tech_id: str) -> None:
        tech = self.repo.get_technology(tech_id)
        if not tech:
            raise NotFoundError("Technology not found")
        self.repo.delete_technology(tech)

    # Milestones
    def list_milestones(self, section: str | None = None) -> list[dict[str, Any]]:
        return [m.to_dict() for m in self.repo.list_milestones(section)]

    def create_milestone(self, data: dict[str, Any]) -> Milestone:
        schema = MilestoneSchema()
        validated = schema.load(data)
        milestone = Milestone(**validated)
        return self.repo.create_milestone(milestone)

    def update_milestone(self, milestone_id: str, data: dict[str, Any]) -> Milestone:
        milestone = self.repo.get_milestone(milestone_id)
        if not milestone:
            raise NotFoundError("Milestone not found")
        schema = MilestoneSchema()
        validated = schema.load(data, partial=True)
        for key, value in validated.items():
            setattr(milestone, key, value)
        return self.repo.update_milestone(milestone)

    def delete_milestone(self, milestone_id: str) -> None:
        milestone = self.repo.get_milestone(milestone_id)
        if not milestone:
            raise NotFoundError("Milestone not found")
        self.repo.delete_milestone(milestone)

    # Steps
    def list_steps(self) -> list[dict[str, Any]]:
        return [s.to_dict() for s in self.repo.list_steps()]

    def create_step(self, data: dict[str, Any]) -> Step:
        schema = StepSchema()
        validated = schema.load(data)
        step = Step(**validated)
        return self.repo.create_step(step)

    def update_step(self, step_id: str, data: dict[str, Any]) -> Step:
        step = self.repo.get_step(step_id)
        if not step:
            raise NotFoundError("Step not found")
        schema = StepSchema()
        validated = schema.load(data, partial=True)
        for key, value in validated.items():
            setattr(step, key, value)
        return self.repo.update_step(step)

    def delete_step(self, step_id: str) -> None:
        step = self.repo.get_step(step_id)
        if not step:
            raise NotFoundError("Step not found")
        self.repo.delete_step(step)

    # Differentiators
    def list_differentiators(self) -> list[dict[str, Any]]:
        return [d.to_dict() for d in self.repo.list_differentiators()]

    def create_differentiator(self, data: dict[str, Any]) -> Differentiator:
        schema = DifferentiatorSchema()
        validated = schema.load(data)
        diff = Differentiator(**validated)
        return self.repo.create_differentiator(diff)

    def update_differentiator(self, diff_id: str, data: dict[str, Any]) -> Differentiator:
        diff = self.repo.get_differentiator(diff_id)
        if not diff:
            raise NotFoundError("Differentiator not found")
        schema = DifferentiatorSchema()
        validated = schema.load(data, partial=True)
        for key, value in validated.items():
            setattr(diff, key, value)
        return self.repo.update_differentiator(diff)

    def delete_differentiator(self, diff_id: str) -> None:
        diff = self.repo.get_differentiator(diff_id)
        if not diff:
            raise NotFoundError("Differentiator not found")
        self.repo.delete_differentiator(diff)

    # Site Settings
    def get_site_settings(self) -> dict[str, Any] | None:
        settings = self.repo.get_site_settings()
        return settings.to_dict() if settings else None

    def update_site_settings(self, data: dict[str, Any]) -> dict[str, Any]:
        schema = SiteSettingSchema()
        validated = schema.load(data, partial=True)
        settings = self.repo.create_or_update_site_settings(validated)
        return settings.to_dict()
