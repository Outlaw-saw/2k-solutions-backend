from datetime import datetime, timezone
from typing import Any

import bcrypt
from flask_jwt_extended import create_access_token, create_refresh_token

from app.extensions import db
from app.models.user import User
from app.repositories.user_repository import UserRepository
from app.schemas.auth import RegisterSchema, LoginSchema
from app.utils.errors import AuthenticationError, ConflictError, ValidationError


class AuthService:
    def __init__(self) -> None:
        self.user_repo = UserRepository()

    def register(self, data: dict[str, Any]) -> dict[str, Any]:
        schema = RegisterSchema()
        validated = schema.load(data)

        existing = self.user_repo.get_by_email(validated["email"])
        if existing:
            raise ConflictError("A user with this email already exists")

        password_hash = bcrypt.hashpw(
            validated["password"].encode("utf-8"),
            bcrypt.gensalt(),
        ).decode("utf-8")

        user = User(
            first_name=validated["first_name"],
            last_name=validated["last_name"],
            email=validated["email"],
            phone=validated["phone"],
            password_hash=password_hash,
            interested_course_slug=validated.get("interested_course_slug"),
            terms_accepted=validated["terms_accepted"],
        )
        self.user_repo.create(user)

        access_token = create_access_token(
            identity=str(user.id),
            additional_claims={"role": user.role},
        )
        refresh_token = create_refresh_token(
            identity=str(user.id),
            additional_claims={"role": user.role},
        )

        return {
            "user": user.to_dict(),
            "access_token": access_token,
            "refresh_token": refresh_token,
        }

    def login(self, data: dict[str, Any]) -> dict[str, Any]:
        schema = LoginSchema()
        validated = schema.load(data)

        user = self.user_repo.get_by_email(validated["email"])
        if not user:
            raise AuthenticationError("Invalid email or password")

        if not user.is_active:
            raise AuthenticationError("Account is deactivated")

        if not bcrypt.checkpw(
            validated["password"].encode("utf-8"),
            user.password_hash.encode("utf-8"),
        ):
            raise AuthenticationError("Invalid email or password")

        user.last_login_at = datetime.now(timezone.utc)
        self.user_repo.update(user)

        access_token = create_access_token(
            identity=str(user.id),
            additional_claims={"role": user.role},
        )
        refresh_token = create_refresh_token(
            identity=str(user.id),
            additional_claims={"role": user.role},
        )

        return {
            "user": user.to_dict(),
            "access_token": access_token,
            "refresh_token": refresh_token,
        }

    def refresh(self, identity: str, role: str) -> dict[str, str]:
        access_token = create_access_token(
            identity=identity,
            additional_claims={"role": role},
        )
        return {"access_token": access_token}
