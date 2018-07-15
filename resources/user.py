import sqlite3
from flask_restful import Resource, reqparse
from models.user import UserModel

class UserRegister(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument(
        "username",
        type=str,
        required=True,
        help="This field can not be empty"
    )
    parser.add_argument(
        "password",
        type=str,
        required=True,
        help="This field can not be empty"
    )
    def post(self):
        data = UserRegister.parser.parse_args()
        user = UserModel(data['username'], data['password'])
        result = user.find_by_username(username=user.username)
        if result is None:
            user.save_to_db()
            return {"message": "User successfully created"}, 201
        else:
            return {"message": "User already exists"}, 400
