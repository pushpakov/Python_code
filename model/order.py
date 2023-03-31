from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client['food_db']
order_collection = db['order']

class Order:
    def __init__(self, name, quantity):
        self.name = name 
        self.quantity = quantity 

    def save(self):
        order_collection.insert_one({
            'name': self.name,
            'quantity': self.quantity,
        }) 

    @staticmethod
    def get_all_orders():
        return list(order_collection.find()) 
