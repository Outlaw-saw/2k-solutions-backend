from marshmallow import Schema, fields, validate


class UserUpdateSchema(Schema):
    first_name = fields.String(validate=validate.Length(min=1, max=100))
    last_name = fields.String(validate=validate.Length(min=1, max=100))
    phone = fields.String(validate=validate.Length(min=5, max=20))
    is_active = fields.Boolean()
    role = fields.String(validate=validate.OneOf(["admin", "student"]))
