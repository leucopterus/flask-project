from flask_restful import Resource, request
from marshmallow import ValidationError

from models.user import UserModel
from schemas.user import UserSchema

user_schema = UserSchema()


class UserRegisterResource(Resource):

    def post(self):
        json_data = request.get_json()

        try:
            data = user_schema.load(json_data)
        except ValidationError as err:
            return err.messages, 400

        if UserModel.find_by_username(data.get('username')):
            return {'message': 'User this such username is already exists'}, 400

        user = UserModel(**data)
        user.save_to_db()

        return {'message': 'User created successfully'}, 201
