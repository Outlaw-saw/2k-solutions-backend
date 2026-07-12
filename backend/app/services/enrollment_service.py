from datetime import datetime, timezone
from typing import Any

from app.models.enrollment import Enrollment
from app.repositories.enrollment_repository import EnrollmentRepository
from app.repositories.course_repository import CourseRepository
from app.schemas.enrollment import EnrollmentCreateSchema, EnrollmentUpdateSchema
from app.utils.errors import NotFoundError, ConflictError, ValidationError


class EnrollmentService:
    def __init__(self) -> None:
        self.enrollment_repo = EnrollmentRepository()
        self.course_repo = CourseRepository()

    def create(self, user_id: str, data: dict[str, Any]) -> Enrollment:
        schema = EnrollmentCreateSchema()
        validated = schema.load(data)

        course = self.course_repo.get_by_slug(validated["course_slug"])
        if not course:
            raise NotFoundError("Course not found")

        existing = self.enrollment_repo.get_by_user_and_course(user_id, str(course.id))
        if existing:
            raise ConflictError("You are already enrolled in this course")

        enrollment = Enrollment(
            user_id=user_id,
            course_id=course.id,
            source_page=validated.get("source_page"),
            status="active",
            started_at=datetime.now(timezone.utc),
        )
        return self.enrollment_repo.create(enrollment)

    def list_by_user(self, user_id: str) -> list[dict[str, Any]]:
        enrollments = self.enrollment_repo.list_by_user(user_id)
        result = []
        for e in enrollments:
            data = e.to_dict()
            course = self.course_repo.get_by_id(str(e.course_id))
            data["course_title"] = course.title if course else None
            data["course_slug"] = course.slug if course else None
            result.append(data)
        return result

    def update(self, enrollment_id: str, data: dict[str, Any]) -> Enrollment:
        enrollment = self.enrollment_repo.get_by_id(enrollment_id)
        if not enrollment:
            raise NotFoundError("Enrollment not found")

        schema = EnrollmentUpdateSchema()
        validated = schema.load(data, partial=True)

        if "status" in validated and validated["status"] == "completed":
            enrollment.completed_at = datetime.now(timezone.utc)

        for key, value in validated.items():
            setattr(enrollment, key, value)
        return self.enrollment_repo.update(enrollment)
