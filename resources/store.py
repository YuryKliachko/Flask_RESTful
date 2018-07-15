from flask_restful import Resource, reqparse
from flask_jwt import JWT, jwt_required
from models.store import StoreModel

class Store(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument(
        "store_id",
        type=int,
        required=True,
        help="This field can not be left blank"
    )

    def get(self, name):
        store = StoreModel.find_by_name(name=name)
        if store is not None:
            return store.json(), 200
        else:
            return {'message': 'The store has not been found'}, 404

    def post(self, name):
        store = StoreModel.find_by_name(name=name)
        if store is not None:
            return {'message': 'The store already exist'}, 400
        else:
            store = StoreModel(name=name)
            store.save_store_to_db()
            return store.json(), 201

    def delete(self, name):
        store = StoreModel.find_by_name(name=name)
        if store is not None:
            store.delete_store_from_db()
            return {'message': 'The store has been deleted'}
        else:
            return {'message': 'The store has not been found'}


class StoreList(Resource):
    def get(self):
        return {'stores': [store.json() for store in StoreModel.query.all()]}
