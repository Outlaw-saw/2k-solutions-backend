from marshmallow import Schema, fields, validate


class ModuleSchema(Schema):
    title = fields.String(required=True, validate=validate.Length(min=1, max=150))
    description = fields.String(allow_none=True)
    icon_class = fields.String(allow_none=True, validate=validate.Length(max=50))
    display_order = fields.Integer(dump_default=0)


class CourseCreateSchema(Schema):
    slug = fields.String(required=True, validate=validate.Length(min=1, max=50))
    title = fields.String(required=True, validate=validate.Length(min=1, max=100))
    subtitle = fields.String(allow_none=True, validate=validate.Length(max=200))
    description = fields.String(allow_none=True)
    definition = fields.String(allow_none=True)
    quote = fields.String(allow_none=True)
    duration_months = fields.Integer(required=True, validate=validate.Range(min=1, max=24))
    num_projects = fields.Integer(dump_default=0, validate=validate.Range(min=0))
    badge = fields.String(allow_none=True, validate=validate.Length(max=50))
    icon_class = fields.String(allow_none=True, validate=validate.Length(max=50))
    curriculum = fields.List(fields.Dict(), allow_none=True)
    career_outcomes = fields.List(fields.String(), allow_none=True)
    history = fields.String(allow_none=True)
    display_order = fields.Integer(dump_default=0)


class CourseUpdateSchema(Schema):
    title = fields.String(validate=validate.Length(min=1, max=100))
    subtitle = fields.String(allow_none=True, validate=validate.Length(max=200))
    description = fields.String(allow_none=True)
    definition = fields.String(allow_none=True)
    quote = fields.String(allow_none=True)
    duration_months = fields.Integer(validate=validate.Range(min=1, max=24))
    num_projects = fields.Integer(validate=validate.Range(min=0))
    badge = fields.String(allow_none=True, validate=validate.Length(max=50))
    icon_class = fields.String(allow_none=True, validate=validate.Length(max=50))
    curriculum = fields.List(fields.Dict(), allow_none=True)
    career_outcomes = fields.List(fields.String(), allow_none=True)
    history = fields.String(allow_none=True)
    is_active = fields.Boolean()
    display_order = fields.Integer()


class ModuleCreateSchema(Schema):
    title = fields.String(required=True, validate=validate.Length(min=1, max=150))
    description = fields.String(allow_none=True)
    icon_class = fields.String(allow_none=True, validate=validate.Length(max=50))
    display_order = fields.Integer(dump_default=0)
