from marshmallow import Schema, fields, validate


class EnrollmentCreateSchema(Schema):
    course_slug = fields.String(required=True, validate=validate.Length(min=1, max=50))
    source_page = fields.String(allow_none=True, validate=validate.Length(max=100))


class EnrollmentUpdateSchema(Schema):
    status = fields.String(validate=validate.OneOf(["pending", "active", "completed", "cancelled"]))
    progress_percent = fields.Integer(validate=validate.Range(min=0, max=100))
