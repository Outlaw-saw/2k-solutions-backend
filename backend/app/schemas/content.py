from marshmallow import Schema, fields, validate


class ServiceSchema(Schema):
    title = fields.String(required=True, validate=validate.Length(min=1, max=100))
    description = fields.String(allow_none=True)
    icon_class = fields.String(allow_none=True, validate=validate.Length(max=50))
    display_order = fields.Integer(dump_default=0)


class TestimonialSchema(Schema):
    student_name = fields.String(required=True, validate=validate.Length(min=1, max=100))
    initials = fields.String(allow_none=True, validate=validate.Length(max=4))
    role = fields.String(allow_none=True, validate=validate.Length(max=100))
    quote = fields.String(required=True)
    rating = fields.Integer(dump_default=5, validate=validate.Range(min=1, max=5))
    display_order = fields.Integer(dump_default=0)


class FAQSchema(Schema):
    question = fields.String(required=True, validate=validate.Length(min=1, max=500))
    answer = fields.String(required=True)
    display_order = fields.Integer(dump_default=0)


class TechnologySchema(Schema):
    name = fields.String(required=True, validate=validate.Length(min=1, max=50))
    icon_class = fields.String(allow_none=True, validate=validate.Length(max=50))
    display_order = fields.Integer(dump_default=0)


class MilestoneSchema(Schema):
    label = fields.String(required=True, validate=validate.Length(min=1, max=100))
    value = fields.Integer(required=True)
    icon_class = fields.String(allow_none=True, validate=validate.Length(max=50))
    section = fields.String(dump_default="milestones", validate=validate.OneOf(["hero", "milestones"]))
    display_order = fields.Integer(dump_default=0)


class StepSchema(Schema):
    step_number = fields.Integer(required=True, validate=validate.Range(min=1, max=20))
    title = fields.String(required=True, validate=validate.Length(min=1, max=200))
    description = fields.String(allow_none=True)
    icon_class = fields.String(allow_none=True, validate=validate.Length(max=50))


class DifferentiatorSchema(Schema):
    number = fields.Integer(required=True, validate=validate.Range(min=1))
    title = fields.String(required=True, validate=validate.Length(min=1, max=100))
    description = fields.String(allow_none=True)
    icon_class = fields.String(allow_none=True, validate=validate.Length(max=50))
    display_order = fields.Integer(dump_default=0)


class SiteSettingSchema(Schema):
    brand_name = fields.String(validate=validate.Length(min=1, max=100))
    tagline = fields.String(allow_none=True, validate=validate.Length(max=200))
    address = fields.String(allow_none=True)
    phone = fields.String(allow_none=True, validate=validate.Length(max=20))
    email = fields.String(allow_none=True, validate=validate.Length(max=255))
    working_hours = fields.String(allow_none=True, validate=validate.Length(max=100))
    social_links = fields.Dict(allow_none=True)
    copyright_year = fields.Integer(allow_none=True)
