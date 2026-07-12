from marshmallow import Schema, fields


class PaginationSchema(Schema):
    page = fields.Int(dump_default=1)
    per_page = fields.Int(dump_default=20)
    total = fields.Int(dump_default=0)
    pages = fields.Int(dump_default=0)
    has_next = fields.Bool(dump_default=False)
    has_prev = fields.Bool(dump_default=False)


class MetaSchema(Schema):
    page = fields.Int()
    per_page = fields.Int()
    total = fields.Int()
    pages = fields.Int()
    has_next = fields.Bool()
    has_prev = fields.Bool()
