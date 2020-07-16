from marshmallow import Schema, fields, EXCLUDE


class AddressSchema(Schema):
    id = fields.Integer(dump_only=True)
    country = fields.String(required=True,
                            error_messages={'required': 'country is required'})
    city = fields.String(required=True,
                         error_messages={'required': 'city is required'})
    street = fields.String(required=True,
                           error_messages={'required': 'street is required'})
    description = fields.String(required=False)

    class Meta:
        unknown = EXCLUDE
