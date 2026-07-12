from typing import Any

from app.extensions import db
from app.models.enrollment import Enrollment
from app.utils.helpers import paginate


class EnrollmentRepository:
    def get_by_id(self, enrollment_id: str) -> Enrollment | None:
        return Enrollment.query.filter_by(id=enrollment_id).first()

    def get_by_user_and_course(self, user_id: str, course_id: str) -> Enrollment | None:
        return Enrollment.query.filter_by(user_id=user_id, course_id=course_id).first()

    def list_by_user(self, user_id: str) -> list[Enrollment]:
        return Enrollment.query.filter_by(user_id=user_id).order_by(Enrollment.created_at.desc()).all()

    def list_paginated(self, user_id: str | None = None) -> dict[str, Any]:
        query = Enrollment.query
        if user_id:
            query = query.filter_by(user_id=user_id)
        query = query.order_by(Enrollment.created_at.desc())
        result = paginate(query)
        result["items"] = [e.to_dict() for e in result["items"]]
        return result

    def create(self, enrollment: Enrollment) -> Enrollment:
        db.session.add(enrollment)
        db.session.commit()
        return enrollment

    def update(self, enrollment: Enrollment) -> Enrollment:
        db.session.commit()
        return enrollment
