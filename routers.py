from resources.item import ItemResource, ItemListResource
from resources.user import UserRegisterResource


def initialize_routers(api):
    api.add_resource(ItemResource, '/item/<string:name>', endpoint='item')
    api.add_resource(ItemListResource, '/items', endpoint='items')
    api.add_resource(UserRegisterResource, '/register', endpoint='user-register')
