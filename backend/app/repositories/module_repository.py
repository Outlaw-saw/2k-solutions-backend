from app.extensions import db
from app.models.module import Module


class ModuleRepository:
    def get_by_course_id(self, course_id: str) -> list[Module]:
        return Module.query.filter_by(course_id=course_id).order_by(Module.display_order).all()

    def create(self, module: Module) -> Module:
        db.session.add(module)
        db.session.commit()
        return module

    def update(self, module: Module) -> Module:
        db.session.commit()
        return module

    def delete(self, module: Module) -> None:
        db.session.delete(module)
        db.session.commit()

    def delete_by_course_id(self, course_id: str) -> None:
        Module.query.filter_by(course_id=course_id).delete()
        db.session.commit()
