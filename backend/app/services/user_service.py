from typing import Any

from app.models.user import User
from app.repositories.user_repository import UserRepository
from app.schemas.user import UserUpdateSchema
from app.utils.errors import NotFoundError


class UserService:
    def __init__(self) -> None:
        self.repo = UserRepository()

    def get_by_id(self, user_id: str) -> User:
        user = self.repo.get_by_id(user_id)
        if not user:
            raise NotFoundError("User not found")
        return user

    def list_paginated(self) -> dict[str, Any]:
        return self.repo.list_paginated()

    def update(self, user_id: str, data: dict[str, Any]) -> User:
        user = self.get_by_id(user_id)
        schema = UserUpdateSchema()
        validated = schema.load(data, partial=True)
        for key, value in validated.items():
            setattr(user, key, value)
        return self.repo.update(user)

    def deactivate(self, user_id: str) -> User:
        user = self.get_by_id(user_id)
        user.is_active = False
        return self.repo.update(user)
