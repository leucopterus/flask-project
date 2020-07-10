from flask import Flask, request, jsonify
from flask_restful import Resource, Api, reqparse
from flask_jwt import JWT, jwt_required

from security import authenticate, identity

app = Flask(__name__)
app.secret_key = 'asdf-9213uf-cHJN(_#@yfhco#@*p:a='

'''
stores_list = [
    {
        'name': 'My Wonderful Store',
        'items': [
            {
                'name': 'My Item',
                'price': 15.99
            }
        ]
    }
]


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/stores', methods=['GET', 'POST'])
def stores():
    if request.method == 'POST':
        request_data = request.get_json()
        new_store = {
            'name': request_data.get('name'),
            'items': []
        }
        stores_list.append(new_store)
        return jsonify(new_store)
    return jsonify({'stores': stores_list})


@app.route('/stores/<string:name>/')
def get_store(name):
    for store in stores_list:
        if store['name'] == name:
            return jsonify(store)
    return jsonify({'message': 'store not found'})


@app.route('/stores/<string:name>/items', methods=['GET', 'POST'])
def items(name):
    if request.method == 'POST':
        request_data = request.get_json()
        for store in stores_list:
            if store['name'] == name:
                new_item = {
                    'name': request_data.get('name'),
                    'price': request_data.get('price')
                }
                store['items'].append(new_item)
                return jsonify(new_item)
    else:
        for store in stores_list:
            if store['name'] == name:
                return jsonify({'items': store['items']})
    return jsonify({'message': 'store not found'})
'''
# -------------------------------------------------------------------------


api = Api(app)
jwt = JWT(app, authenticate, identity)

items_list = []


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
        item = next(filter(lambda x: x['name'] == name, items_list), None)
        return {'item': item}, 200 if item else 404

    @jwt_required()
    def post(self, name):
        if next(filter(lambda x: x['name'] == name, items_list), None):
            return {'message': f'An item with name {name} is already exists'}, 400
        data = self.parser.parse_args()
        item = {'name': name, 'price': data['price']}
        items_list.append(item)
        return item, 201

    @jwt_required()
    def delete(self, name):
        global items_list
        items_list = list(filter(lambda x: x.get('name') != name, items_list))
        return {'message': 'item deleted'}

    @jwt_required()
    def put(self, name):
        data = self.parser.parse_args()

        item = next(filter(lambda x: x['name'] == name, items_list), None)
        if item is None:
            item = {'name': name, 'price': data.get('price')}
            items_list.append(item)
        else:
            item.update(data)
        return item


class ItemList(Resource):
    @jwt_required()
    def get(self):
        return {'items': items_list}


api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList, '/items/')


if __name__ == '__main__':
    app.run(debug=True)
