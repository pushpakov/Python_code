from flask import Flask, url_for 
from pymongo import MongoClient 
from bson import json_util
from bson.json_util import dumps
from bson.objectid import ObjectId
from flask import jsonify,request
from werkzeug.security import generate_password_hash,check_password_hash
from flask.json import JSONEncoder
from bson import ObjectId 
import math 
from dataclasses import dataclass 
from typing import List 

 
app = Flask(__name__)
app.secret_key = "secretkey"
 
client = MongoClient('mongodb://localhost:27017/')
db = client['InstaLike']
collection = db['User']

# class to customize the json object serilization 
class CustomJSONEncoder(JSONEncoder):
    def default(self, obj):
        if isinstance(obj, ObjectId):
            return str(obj) 
        return super().default(obj)
# setting json encoder default as CustomJSONEncoder
app.json_encoder = CustomJSONEncoder

@dataclass
class Person:
    name: str
    email: str
    password: str
    followers: List[any] 

# add user 
@app.route('/add', methods=['POST'])
def add_user():
    _json = request.json
    _name = _json['name']
    _email = _json['email']
    _password = _json['password']

    if _name and _email and _password and request.method == 'POST':
        _hashed_password = generate_password_hash(_password)

        user_data = Person(name =_name, email = _email, password =  _hashed_password, followers = [])
        # user_data = {'name': _name, 'email': _email, 'password': _hashed_password, 'followers': []}

        result = collection.insert_one(user_data.__dict__) 

        resp = jsonify('User Added successfully')
        resp.status_code = 200

        return resp 

    else:
        return not_found()


# method the hande error of not found 
@app.errorhandler(404)
def not_found(error=None):
    message = {
        'status':404,
        'message':'Not Found' + request.url
    }
    resp = jsonify(message)
 
    resp.status_code = 404
 
    return resp



# find all  the user and adding pagination 
@app.route('/users')
def users():
    page = int(request.args.get('page', 1))
    limit = int(request.args.get('limit', 10))

    offset = (page - 1) * limit

    users = collection.find().skip(offset).limit(limit)

    data = list(users)

    total = collection.count_documents({})

    pages = math.ceil(total / limit)

    response = {
        'data': data,
        'page': page,
        'limit': limit,
        'total': total,
        'pages': pages
    }
    return jsonify(response)


@app.route('/users/<id>')
def user(id):
    user = collection.find_one({'_id':ObjectId(id)})
    if user is None:
        return not_found() 
    return user 


@app.route('/delete/<id>',methods=['DELETE'])
def delete_user(id):
    collection.delete_one({'_id':ObjectId(id)})
    resp = jsonify("User deleted successfully")
    resp.status_code = 200
    return resp

 
# update a particular user using user id 
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



# follow a particular user 
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

    


# find total followers of a particular user and add pagination
@app.route('/followers/<user_id>')
def get_followers(user_id):
    page = int(request.args.get('page', 1))
    per_page = int(request.args.get('per_page', 10))
    
    user = collection.find_one({'_id': ObjectId(user_id)})
    if user:
        followers = user.get('followers', [])
        total_followers = len(followers)
        
        start_index = (page - 1) * per_page
        end_index = start_index + per_page
        
        followers_data = []
        for follower in followers[start_index:end_index]:
            follower.pop('password', None)
            followers_data.append(follower)

        pagination = {
            'total_followers': total_followers,
            'per_page': per_page,
            'current_page': page,
            'last_page': math.ceil(total_followers / per_page),
            'prev_page': url_for('get_followers', user_id=user_id, page=page-1, per_page=per_page) if page > 1 else None,
            'next_page': url_for('get_followers', user_id=user_id, page=page+1, per_page=per_page) if end_index < total_followers else None,
            'first_page': url_for('get_followers', user_id=user_id, page=1, per_page=per_page),
            'last_page': url_for('get_followers', user_id=user_id, page=math.ceil(total_followers / per_page), per_page=per_page)
        }
        
        return jsonify({'followers': followers_data, 'pagination': pagination})
    else:
        return not_found()


if __name__ == "__main__":
    app.run(debug=True)





