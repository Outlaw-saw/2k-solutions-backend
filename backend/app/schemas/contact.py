from marshmallow import Schema, fields, validate


class ContactCreateSchema(Schema):
    name = fields.String(required=True, validate=validate.Length(min=1, max=150))
    email = fields.Email(required=True, validate=validate.Length(max=255))
    phone = fields.String(allow_none=True, validate=validate.Length(max=20))
    subject = fields.String(allow_none=True, validate=validate.OneOf(
        ["course", "corporate", "internship", "placement", "other", ""]
    ))
    message = fields.String(required=True, validate=validate.Length(min=1))
