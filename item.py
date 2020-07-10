import sqlite3

from flask_jwt import jwt_required
from flask_restful import Resource, reqparse


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
        item = self.find_by_name(name)
        return (item, 200) if item else ({'message': 'Item not found'}, 404)

    @jwt_required()
    def post(self, name):
        if self.find_by_name(name):
            return {'message': f'An item with name {name} is already exists'}, 400
        data = self.parser.parse_args()
        item = {'name': name, 'price': data['price']}

        try:
            self.insert(item)
        except:
            return {'message': 'An error occurred inserting the item'}, 500

        return item, 201

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

        item = self.find_by_name(name)
        updated_item = {'name': name, 'price': data.get('price')}
        try:
            if item is None:
                self.insert(updated_item)
            else:
                self.update(updated_item)
        except:
            return {'message': 'An error occurred updating the item'}, 500
        return updated_item

    @classmethod
    def find_by_name(cls, name):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = 'SELECT * FROM items WHERE name=?'
        result = cursor.execute(query, (name,))
        item = result.fetchone()
        connection.close()
        return item

    @classmethod
    def insert(cls, item):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()
        query = 'INSERT INTO items VALUES (?, ?)'
        cursor.execute(query, (item['name'], item['price']))
        connection.commit()
        connection.close()

    @classmethod
    def update(cls, item):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()
        query = 'UPDATE items SET price=? WHERE name=?'
        cursor.execute(query, (item['price'], item['name']))
        connection.commit()
        connection.close()


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
