from flask import Flask, request, jsonify
from flask_restful import Resource, Api

app = Flask(__name__)

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


api = Api(app)


class Student(Resource):
    def get(self, name):
        return {'student': name}


api.add_resource(Student, '/student/<string:name>')


if __name__ == '__main__':
    app.run()
