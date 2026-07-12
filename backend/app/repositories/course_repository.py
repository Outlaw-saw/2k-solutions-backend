from typing import Any

from app.extensions import db
from app.models.course import Course
from app.utils.helpers import apply_search, apply_sorting, paginate


class CourseRepository:
    def get_by_id(self, course_id: str) -> Course | None:
        return Course.query.filter_by(id=course_id).first()

    def get_by_slug(self, slug: str) -> Course | None:
        return Course.query.filter_by(slug=slug).first()

    def list_active(self) -> list[Course]:
        return Course.query.filter_by(is_active=True).order_by(Course.display_order).all()

    def list_paginated(self) -> dict[str, Any]:
        query = Course.query
        query = apply_search(query, Course, ["title", "subtitle", "slug"])
        query = apply_sorting(query, Course)
        result = paginate(query)
        result["items"] = [c.to_dict() for c in result["items"]]
        return result

    def create(self, course: Course) -> Course:
        db.session.add(course)
        db.session.commit()
        return course

    def update(self, course: Course) -> Course:
        db.session.commit()
        return course

    def delete(self, course: Course) -> None:
        db.session.delete(course)
        db.session.commit()
