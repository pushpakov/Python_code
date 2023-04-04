from flask import Flask, jsonify, request, url_for
import math 
from pymongo import MongoClient
from werkzeug.security import generate_password_hash
from typing import List
from bson import ObjectId 
# from bson.json_util import dumps, loads
from models.model import Person 
from logs.logger import setup_logger 
from validations.validation import PersonSchema 

app = Flask(__name__)
app.secret_key = "secretkey"

client = MongoClient('mongodb://localhost:27017/')
db = client['InstaLike']
collection = db['User']
 
logger = setup_logger()

person_schema = PersonSchema()

# method to handle not found error
@app.errorhandler(404)
def not_found(error=None):
    message = {
        'status': 404,
        'message': 'Not Found: ' + request.url
    }
    resp = jsonify(message)
    resp.status_code = 404
    return resp

# method to handle server error
@app.errorhandler(500)
def internal_server_error(error=None):
    message = {
        'status': 500,
        'message': 'Internal Server Error: Please contact the service provider'
    }
    resp = jsonify(message)
    resp.status_code = 500
    return resp

# add user
@app.route('/add', methods=['POST'])
def add_user():
    try:
        json_data = request.get_json()
        if not json_data:
            return not_found()

        person_data = person_schema.load(json_data)

        if not person_data:
            return not_found()

        hashed_password = generate_password_hash(person_data.password)

        user_data = Person(name=person_data.name, email=person_data.email, password=hashed_password)

        result = collection.insert_one(user_data.__dict__)

        resp = jsonify('User Added successfully')
        resp.status_code = 200

        return resp

    except Exception as e:
        # print(e) 
        logger.error(str(e)) 
        return internal_server_error()



# find all  the user and adding pagination 
@app.route('/users')
def users():
    try:
        page = int(request.args.get('page', 1))
        limit = int(request.args.get('limit', 10))

        offset = (page - 1) * limit

        users = collection.find().skip(offset).limit(limit)
        # print(users) 
        total = collection.count_documents({})
        if total == 0:
            return not_found() 
        data = []
        for user in users:
            person = Person(user['name'], user['email'], user['password'], user['followers'])
            person.id = str(user['_id'])
            data.append(person)

        

        pages = math.ceil(total / limit) 
         
        response = {
            'data': [person.__dict__ for person in data],
            'page': page,
            'limit': limit,
            'total': total,
            'pages': pages
        }
        return jsonify(response)

    except Exception as e:
        print(e)
        return internal_server_error() 




# find user using user id 
@app.route('/users/<id>')
def user(id):
    try:
        user_data = collection.find_one({'_id': ObjectId(id)})
        if user_data is None:
            return not_found()
        
        user = Person(name=user_data['name'], email=user_data['email'], password=user_data['password'], followers=user_data['followers'])
        user._id = str(user_data['_id']) 

        return jsonify(user.__dict__) 
    
    except Exception as e:
        print(e)
        return internal_server_error()



# delete user using user id 
@app.route('/delete/<id>', methods=['DELETE'])
def delete_user(id):
    try:
        result = collection.delete_one({'_id': ObjectId(id)})
        if result.deleted_count == 0:
            return not_found() 
        else:
            resp = jsonify("User deleted successfully")
            resp.status_code = 200
            return resp

    except Exception as e:
        print(e)
        return internal_server_error() 

 
# update a particular user using user id 
@app.route('/update/<id>', methods=['PUT']) 
def update_user(id):
    try:
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
 
            return jsonify("User updated successfully")  
 
        else:
            return not_found() 
    except Exception as e:
        print(e) 
        return internal_server_error() 



# follow a particular user 
@app.route('/follow', methods=['POST'])
def add_follower():
    try:
        _json = request.json
        _user_id = _json['user_id']
        _follower_id = _json['follower_id']

        if _user_id and _follower_id and request.method == 'POST':
            user_data = collection.find_one({'_id': ObjectId(_user_id)})
            follower_data = collection.find_one({'_id': ObjectId(_follower_id)}) 
            print(type(follower_data)) 
            # print(user_data) 
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
    except Exception as e:
        # print(e) 
        return internal_server_error() 

    


# find total followers of a particular user and add pagination
@app.route('/followers/<user_id>')
def get_followers(user_id):
    try: 
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
    except Exception as e:
        return internal_server_error()


if __name__ == "__main__":
    app.run(debug=True)





