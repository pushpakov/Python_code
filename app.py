from flask import Flask
from pymongo import MongoClient 
from bson import json_util
from bson.json_util import dumps
from bson.objectid import ObjectId
from flask import jsonify,request
from werkzeug.security import generate_password_hash,check_password_hash
from flask.json import JSONEncoder
from bson import ObjectId 
 
app = Flask(__name__)
app.secret_key = "secretkey"
 
client = MongoClient('mongodb://localhost:27017/')
db = client['InstaLike']
collection = db['User']


class CustomJSONEncoder(JSONEncoder):
    def default(self, obj):
        if isinstance(obj, ObjectId):
            return str(obj)
        return super().default(obj)

app.json_encoder = CustomJSONEncoder

@app.route('/add', methods=['POST'])
def add_user():
    _json = request.json
    _name = _json['name']
    _email = _json['email']
    _password = _json['password']

    if _name and _email and _password and request.method == 'POST':
        _hashed_password = generate_password_hash(_password)

        user_data = {'name': _name, 'email': _email, 'password': _hashed_password, 'followers': []}

        result = collection.insert_one(user_data)

        resp = jsonify('User Added successfully')
        resp.status_code = 200

        return resp 

    else:
        return not_found()



@app.errorhandler(404)
def not_found(error=None):
    message = {
        'status':404,
        'message':'Not Found' + request.url
    }
    resp = jsonify(message)
 
    resp.status_code = 404
 
    return resp


@app.route('/users')
def users():
    users = collection.find()
    resp = dumps(users)
    return resp


@app.route('/users/<id>')
def user(id):
    user = collection.find_one({'_id':ObjectId(id)})
    resp = dumps(user)
    return resp


@app.route('/delete/<id>',methods=['DELETE'])
def delete_user(id):
    collection.delete_one({'_id':ObjectId(id)})
    resp = jsonify("User deleted successfully")
    resp.status_code = 200
    return resp



@app.route('/update/<id>', methods=['PUT'])
def update_user(id):
    _id = id
    _json = request.json
    
    update_data = {}

    if 'name' in _json:
        update_data['name'] = _json['name']
    
    if 'email' in _json:
        update_data['email'] = _json['email']
    
    if 'password' in _json:
        update_data['password'] = generate_password_hash(_json['password'])
 
    if _id and update_data and request.method == "PUT":
        collection.update_one({'_id':ObjectId(_id)}, {'$set': update_data})
 
        resp = jsonify("User updated successfully")
        resp.status_code = 200
 
        return resp
 
    else:
        return not_found()

import json

@app.route('/follow', methods=['POST'])
def add_follower():
    _json = request.json
    _user_id = _json['user_id']
    _follower_id = _json['follower_id']

    if _user_id and _follower_id and request.method == 'POST':
        user_data = collection.find_one({'_id': ObjectId(_user_id)})
        follower_data = collection.find_one({'_id': ObjectId(_follower_id)}) 
        print(type(follower_data)) 
        if user_data:
            user_data['followers'].append(follower_data)

            collection.update_one({'_id': ObjectId(_user_id)}, {'$set': {'followers': user_data['followers']}})

            resp = jsonify('Follower Added successfully')
            resp.status_code = 200

            return resp
        else:
            return not_found() 

    else:
        return not_found()

    


@app.route('/followers/<user_id>')
def get_followers(user_id):
    user = collection.find_one({'_id': ObjectId(user_id)})
    # print(user) 
    if user:
        followers = user.get('followers', [])
        followers_data = []
        for follower in followers:
            # Exclude the password field from the serialized document
            follower.pop('password', None)
            followers_data.append(follower)
        return jsonify(followers_data)
    else:
        return not_found()



if __name__ == "__main__":
    app.run(debug=True)





