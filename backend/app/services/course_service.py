from typing import Any

from app.models.course import Course
from app.models.module import Module
from app.repositories.course_repository import CourseRepository
from app.repositories.module_repository import ModuleRepository
from app.schemas.course import CourseCreateSchema, CourseUpdateSchema, ModuleCreateSchema
from app.utils.errors import NotFoundError, ConflictError


class CourseService:
    def __init__(self) -> None:
        self.course_repo = CourseRepository()
        self.module_repo = ModuleRepository()

    def get_by_slug(self, slug: str) -> Course:
        course = self.course_repo.get_by_slug(slug)
        if not course:
            raise NotFoundError("Course not found")
        return course

    def list_active(self) -> list[dict[str, Any]]:
        courses = self.course_repo.list_active()
        return [c.to_dict() for c in courses]

    def list_paginated(self) -> dict[str, Any]:
        return self.course_repo.list_paginated()

    def create(self, data: dict[str, Any]) -> Course:
        schema = CourseCreateSchema()
        validated = schema.load(data)

        existing = self.course_repo.get_by_slug(validated["slug"])
        if existing:
            raise ConflictError("A course with this slug already exists")

        modules_data = validated.pop("modules", [])
        course = Course(**validated)
        self.course_repo.create(course)

        for i, mod_data in enumerate(modules_data):
            mod_schema = ModuleCreateSchema()
            mod_validated = mod_schema.load(mod_data)
            module = Module(
                course_id=course.id,
                **mod_validated,
                display_order=mod_validated.get("display_order", i + 1),
            )
            self.module_repo.create(module)

        return course

    def update(self, slug: str, data: dict[str, Any]) -> Course:
        course = self.get_by_slug(slug)
        schema = CourseUpdateSchema()
        validated = schema.load(data, partial=True)
        for key, value in validated.items():
            setattr(course, key, value)
        return self.course_repo.update(course)

    def get_with_modules(self, slug: str) -> dict[str, Any]:
        course = self.get_by_slug(slug)
        course_data = course.to_dict()
        modules = self.module_repo.get_by_course_id(str(course.id))
        course_data["modules"] = [m.to_dict() for m in modules]
        return course_data
