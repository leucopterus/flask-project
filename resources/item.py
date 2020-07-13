from flask_jwt import jwt_required
from flask_restful import Resource, reqparse

from models.item import ItemModel
from schemas.item import ItemSchema

item_schema = ItemSchema()
items_schema = ItemSchema(many=True)


class ItemResource(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument(
        'price',
        type=float,
        required=True,
        help='This field cannot be left blank!'
    )

    @jwt_required()
    def get(self, name):
        item = ItemModel.find_by_name(name)
        item_result = item_schema.dump(item)
        return (item_result, 200) if item else ({'message': 'Item not found'}, 404)

    @jwt_required()
    def post(self, name):
        if ItemModel.find_by_name(name):
            return {'message': f'An item with name {name} is already exists'}, 400
        data = self.parser.parse_args()
        item_validated = item_schema.load(name, **data)
        item = ItemModel(**item_validated)

        try:
            item.save_to_db()
        except:
            return {'message': 'An error occurred inserting the item'}, 500

        return item_validated, 201

    @jwt_required()
    def delete(self, name):
        item = ItemModel.find_by_name(name)
        if item:
            item.delete_from_db()

        return {'message': 'item deleted'}

    @jwt_required()
    def put(self, name):
        data = self.parser.parse_args()

        item = ItemModel.find_by_name(name)

        if item is None:
            item = ItemModel(name, **data)
        else:
            item.price = data['price']

        item.save_to_db()

        return item.json()


class ItemListResource(Resource):
    @jwt_required()
    def get(self):
        items = ItemModel.query.all()
        result = items_schema.dump(items)
        return {'items': result}
