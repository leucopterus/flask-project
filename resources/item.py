import sqlite3

from flask_jwt import jwt_required
from flask_restful import Resource, reqparse

from models.item import ItemModel


class Item(Resource):
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
        return (item.json(), 200) if item else ({'message': 'Item not found'}, 404)

    @jwt_required()
    def post(self, name):
        if ItemModel.find_by_name(name):
            return {'message': f'An item with name {name} is already exists'}, 400
        data = self.parser.parse_args()
        item = ItemModel(name, data['price'])

        try:
            item.insert()
        except:
            return {'message': 'An error occurred inserting the item'}, 500

        return item.json(), 201

    @jwt_required()
    def delete(self, name):

        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()
        query = 'DELETE FROM items WHERE name=?'
        cursor.execute(query, (name,))
        connection.commit()
        connection.close()

        return {'message': 'item deleted'}

    @jwt_required()
    def put(self, name):
        data = self.parser.parse_args()

        item = ItemModel.find_by_name(name)
        updated_item = ItemModel(name, data['price'])
        try:
            if item is None:
                updated_item.insert()
            else:
                updated_item.update()
        except:
            return {'message': 'An error occurred updating the item'}, 500
        return updated_item.json()


class ItemList(Resource):
    @jwt_required()
    def get(self):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()
        query = 'SELECT * FROM items'
        result = cursor.execute(query)
        items = [{'name': row[0], 'price': row[1]} for row in result]
        connection.close()

        return {'items': items}
