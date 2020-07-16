from marshmallow import Schema, fields, EXCLUDE

from api.schemas.user import UserSchema
from api.schemas.address import AddressSchema


class PublisherSchema(Schema):
    id = fields.Integer(dump_only=True)
    name = fields.String()
    address = fields.Nested(AddressSchema(
        only=('id',)
    ))
    owner = fields.Nested(UserSchema(
        load_only=('id',),
        dump_only=('id', 'first_name', 'last_name')
    ))

    class Meta:
        unknown = EXCLUDE
