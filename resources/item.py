from flask_restful import Resource, reqparse
from flask_jwt import JWT, jwt_required
from models.item import ItemModel

class Item(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument(
        "price",
        type=float,
        required=True,
        help="This field can not be left blank"
    )
    parser.add_argument(
        "store_id",
        type=int,
        required=True,
        help="This field can not be left blank"
    )


    @jwt_required()
    def get(self, name):
        item = ItemModel.find_by_name(name)
        if item is not None:
            return item.json(), 200
        else:
            return {"message": "Item has not been found"}, 404

    def post(self, name):
        item = ItemModel.find_by_name(name)
        if item is not None:
            return "The item {} already exists".format(name), 400
        else:
            data = Item.parser.parse_args()
            item = ItemModel(name=name, price=data['price'], store_id=data['store_id'])
            try:
                item.save_item_to_db()
                return item.json(), 201
            except:
                return {"message": "An error occured"}, 500


    @jwt_required()
    def delete(self, name):
        item = ItemModel.find_by_name(name)
        if item is not None:
            item.delete_item_from_db()
            return {"message": "item deleted"}
        else:
            return {"message": "item does not exist"}, 404


    def put(self, name):
        data = Item.parser.parse_args()
        item = ItemModel.find_by_name(name)
        if item is None:
            item = ItemModel(name, price=data['price'], store_id=data['store_id'])
        else:
            item.price = data['price']
            item.store_id = data['store_id']
        item.save_item_to_db()
        return item.json()


class ItemList(Resource):
    @jwt_required()
    def get(self):
        return {'items': [item.json() for item in ItemModel.query.all()]}