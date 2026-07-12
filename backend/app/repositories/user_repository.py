from typing import Any

from app.extensions import db
from app.models.user import User
from app.utils.helpers import apply_search, apply_sorting, paginate


class UserRepository:
    def get_by_id(self, user_id: str) -> User | None:
        return User.query.filter_by(id=user_id).first()

    def get_by_email(self, email: str) -> User | None:
        return User.query.filter_by(email=email).first()

    def list_all(self) -> list[User]:
        return User.query.order_by(User.created_at.desc()).all()

    def list_paginated(self) -> dict[str, Any]:
        query = User.query
        query = apply_search(query, User, ["first_name", "last_name", "email", "phone"])
        query = apply_sorting(query, User)
        result = paginate(query)
        result["items"] = [u.to_dict() for u in result["items"]]
        return result

    def create(self, user: User) -> User:
        db.session.add(user)
        db.session.commit()
        return user

    def update(self, user: User) -> User:
        db.session.commit()
        return user

    def delete(self, user: User) -> None:
        db.session.delete(user)
        db.session.commit()
