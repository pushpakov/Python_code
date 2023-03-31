from flask import Flask, jsonify, request
from model.menu import Menu
from model.order import Order
from flask.json import JSONEncoder
from bson import ObjectId
# import json

class CustomJSONEncoder(JSONEncoder):
    def default(self, obj):
        if isinstance(obj, ObjectId):
            return str(obj)
        return JSONEncoder.default(self, obj)


app = Flask(__name__)
app.json_encoder = CustomJSONEncoder 


@app.route('/menu', methods = ['GET', 'POST']) 
def menu(): 
    if request.method == 'POST':
        food_name = request.json['food_name']
        # item_id = str(uuid.uuid4()) # generate a UUID 
        price = request.json['price']   
        menu = Menu(food_name,price)  
        menu.save() 
        # serialized_menu = json.dumps(menu.__dict__)
        return jsonify({'message': 'Menu Created successfully.', 'data' : menu.__dict__})   
    else:
        items = Menu.get_all_items()
        serialized_items = [item for item in items]
        return jsonify(serialized_items)   

@app.route('/menu/<string:item_id>') 
def get_item(item_id):
    item = Menu.get_item(item_id)
    return jsonify(item)

@app.route('/order', methods=['GET', 'POST'])
def orders():
    if request.method == 'POST':
        name = request.json['name']
        quantity = request.json['quantity']
        order = Order(name,quantity)  
        order.save()
        return jsonify({'message': 'Order placed successfully.', 'data' : order.__dict__})
    else:
        orders = Order.get_all_orders()
        serilized_order = [order for order in orders]
        return jsonify(serilized_order) 

if __name__ == '__main__':
    app.run(debug=True)
