from resources.item import Item, ItemList
from resources.user import UserRegister


def initialize_routers(api):
    api.add_resource(Item, '/item/<string:name>', endpoint='item')
    api.add_resource(ItemList, '/items', endpoint='items')
    api.add_resource(UserRegister, '/register', endpoint='user-register')
