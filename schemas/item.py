from marshmallow import Schema, fields, ValidationError


def must_not_be_blank(data):
    if not data:
        raise ValidationError('Data not provided')


class ItemSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(validate=must_not_be_blank)
    price = fields.Float(validate=must_not_be_blank)
