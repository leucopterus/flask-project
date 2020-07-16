from marshmallow import Schema, fields, validate, EXCLUDE

from .utils import password_validation


class UserSchema(Schema):
    id = fields.Integer(dump_only=True)
    username = fields.String(required=True,
                             error_messages={'required': 'username is required'},
                             validate=validate.Length(min=5))
    first_name = fields.String(required=True,
                               error_messages={'required': 'first name is required'},)
    last_name = fields.String(required=True,
                              error_messages={'required': 'last name is required'},)
    email = fields.Email(required=True,
                         error_messages={'required': 'last name is required'},)
    password = fields.String(load_only=True,
                             required=True,
                             error_messages={'required': 'password is required'},
                             validate=password_validation)
    description = fields.String(required=False)
    created_at = fields.DateTime(required=False, dump_only=True)
    is_active = fields.Boolean(required=False, default=True)

    class Meta:
        unknown = EXCLUDE
