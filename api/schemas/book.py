from marshmallow import Schema, fields, EXCLUDE

from api.schemas.user import UserSchema
from api.schemas.publisher import PublisherSchema


class TableSchema(Schema):
    user_id = fields.Integer()
    book_id = fields.Integer()


class BookSchema(Schema):
    id = fields.Integer(dump_only=True)
    title = fields.String(required=True,
                          error_messages={'message': 'Book\'s title is required.'})
    authors = fields.Nested(UserSchema(
                            load_only=('id',),
                            dump_only=('first_name', 'last_name')
                            ),
                            many=True)
    publisher = fields.Nested(PublisherSchema(
                              load_only=('id',),
                              dump_only=('name',)),
                              )

    class Meta:
        unknown = EXCLUDE
