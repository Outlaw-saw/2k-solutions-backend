from typing import Any

from app.extensions import db
from app.models.service import Service
from app.models.testimonial import Testimonial
from app.models.faq import FAQ
from app.models.technology import Technology
from app.models.milestone import Milestone
from app.models.step import Step
from app.models.differentiator import Differentiator
from app.models.site_setting import SiteSetting


class ContentRepository:
    # Services
    def list_services(self) -> list[Service]:
        return Service.query.filter_by(is_active=True).order_by(Service.display_order).all()

    def get_service(self, service_id: str) -> Service | None:
        return Service.query.filter_by(id=service_id).first()

    def create_service(self, service: Service) -> Service:
        db.session.add(service)
        db.session.commit()
        return service

    def update_service(self, service: Service) -> Service:
        db.session.commit()
        return service

    def delete_service(self, service: Service) -> None:
        db.session.delete(service)
        db.session.commit()

    # Testimonials
    def list_testimonials(self) -> list[Testimonial]:
        return Testimonial.query.filter_by(is_active=True).order_by(Testimonial.display_order).all()

    def get_testimonial(self, testimonial_id: str) -> Testimonial | None:
        return Testimonial.query.filter_by(id=testimonial_id).first()

    def create_testimonial(self, testimonial: Testimonial) -> Testimonial:
        db.session.add(testimonial)
        db.session.commit()
        return testimonial

    def update_testimonial(self, testimonial: Testimonial) -> Testimonial:
        db.session.commit()
        return testimonial

    def delete_testimonial(self, testimonial: Testimonial) -> None:
        db.session.delete(testimonial)
        db.session.commit()

    # FAQs
    def list_faqs(self) -> list[FAQ]:
        return FAQ.query.filter_by(is_active=True).order_by(FAQ.display_order).all()

    def get_faq(self, faq_id: str) -> FAQ | None:
        return FAQ.query.filter_by(id=faq_id).first()

    def create_faq(self, faq: FAQ) -> FAQ:
        db.session.add(faq)
        db.session.commit()
        return faq

    def update_faq(self, faq: FAQ) -> FAQ:
        db.session.commit()
        return faq

    def delete_faq(self, faq: FAQ) -> None:
        db.session.delete(faq)
        db.session.commit()

    # Technologies
    def list_technologies(self) -> list[Technology]:
        return Technology.query.order_by(Technology.display_order).all()

    def get_technology(self, tech_id: str) -> Technology | None:
        return Technology.query.filter_by(id=tech_id).first()

    def create_technology(self, tech: Technology) -> Technology:
        db.session.add(tech)
        db.session.commit()
        return tech

    def update_technology(self, tech: Technology) -> Technology:
        db.session.commit()
        return tech

    def delete_technology(self, tech: Technology) -> None:
        db.session.delete(tech)
        db.session.commit()

    # Milestones
    def list_milestones(self, section: str | None = None) -> list[Milestone]:
        query = Milestone.query.order_by(Milestone.display_order)
        if section:
            query = query.filter_by(section=section)
        return query.all()

    def get_milestone(self, milestone_id: str) -> Milestone | None:
        return Milestone.query.filter_by(id=milestone_id).first()

    def create_milestone(self, milestone: Milestone) -> Milestone:
        db.session.add(milestone)
        db.session.commit()
        return milestone

    def update_milestone(self, milestone: Milestone) -> Milestone:
        db.session.commit()
        return milestone

    def delete_milestone(self, milestone: Milestone) -> None:
        db.session.delete(milestone)
        db.session.commit()

    # Steps
    def list_steps(self) -> list[Step]:
        return Step.query.order_by(Step.step_number).all()

    def get_step(self, step_id: str) -> Step | None:
        return Step.query.filter_by(id=step_id).first()

    def create_step(self, step: Step) -> Step:
        db.session.add(step)
        db.session.commit()
        return step

    def update_step(self, step: Step) -> Step:
        db.session.commit()
        return step

    def delete_step(self, step: Step) -> None:
        db.session.delete(step)
        db.session.commit()

    # Differentiators
    def list_differentiators(self) -> list[Differentiator]:
        return Differentiator.query.order_by(Differentiator.display_order).all()

    def get_differentiator(self, diff_id: str) -> Differentiator | None:
        return Differentiator.query.filter_by(id=diff_id).first()

    def create_differentiator(self, diff: Differentiator) -> Differentiator:
        db.session.add(diff)
        db.session.commit()
        return diff

    def update_differentiator(self, diff: Differentiator) -> Differentiator:
        db.session.commit()
        return diff

    def delete_differentiator(self, diff: Differentiator) -> None:
        db.session.delete(diff)
        db.session.commit()

    # Site Settings
    def get_site_settings(self) -> SiteSetting | None:
        return SiteSetting.query.first()

    def create_or_update_site_settings(self, data: dict[str, Any]) -> SiteSetting:
        settings = self.get_site_settings()
        if settings:
            for key, value in data.items():
                if hasattr(settings, key):
                    setattr(settings, key, value)
        else:
            settings = SiteSetting(**data)
            db.session.add(settings)
        db.session.commit()
        return settings
