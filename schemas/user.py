from marshmallow import Schema, fields, ValidationError


def must_not_be_blank(data):
    if not data:
        raise ValidationError('Data not provided')


class UserSchema(Schema):
    id = fields.Int(dump_only=True)
    username = fields.Str(validate=must_not_be_blank)
    password = fields.Float(validate=must_not_be_blank)
