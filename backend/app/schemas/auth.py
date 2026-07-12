from marshmallow import Schema, fields, validate, validates, ValidationError


class RegisterSchema(Schema):
    first_name = fields.String(required=True, validate=validate.Length(min=1, max=100))
    last_name = fields.String(required=True, validate=validate.Length(min=1, max=100))
    email = fields.Email(required=True, validate=validate.Length(max=255))
    phone = fields.String(required=True, validate=validate.Length(min=5, max=20))
    password = fields.String(required=True, validate=validate.Length(min=6, max=128))
    interested_course_slug = fields.String(allow_none=True, validate=validate.Length(max=50))
    terms_accepted = fields.Boolean(required=True)

    @validates("terms_accepted")
    def validate_terms(self, value: bool) -> None:
        if not value:
            raise ValidationError("You must accept the terms and conditions")

    @validates("interested_course_slug")
    def validate_course(self, value: str | None) -> None:
        valid_slugs = [
            "software-development", "web-development", "data-analytics",
            "cloud-computing", "ai-machine-learning", "app-development",
        ]
        if value and value not in valid_slugs:
            raise ValidationError(f"Invalid course slug. Must be one of: {', '.join(valid_slugs)}")


class LoginSchema(Schema):
    email = fields.Email(required=True)
    password = fields.String(required=True, validate=validate.Length(min=1))


class RefreshSchema(Schema):
    refresh_token = fields.String(required=True)
