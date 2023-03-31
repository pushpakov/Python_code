from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client['food_db']
menu_collection = db['menu']

class Menu:
    def __init__(self, food_name, price):
        self.food_name = food_name
        self.price = price

    def to_dict(self):
        return {
            'food_name': self.food_name,
            'price': self.price,
        }
    
    def save(self):
        menu_collection.insert_one({
            'food_name': self.food_name, 
            'price' : self.price 
        }) 
    @staticmethod 
    def get_all_items():
        return list(menu_collection.find())

    @staticmethod
    def get_item(item_id):
        return menu_collection.find_one({'_id': item_id})
