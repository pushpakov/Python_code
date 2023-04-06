import unittest
from bson.objectid import ObjectId
from app import app
 
class FlaskAppTest(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

    def test_add_user(self):
        data = { 
            "name": "Test User",
            "email": "testuser@example.com",
            "password": "password"
        }
        response = self.client.post('/add', json=data)
        print(response.json)
        self.assertEqual(response.status_code, 201)   
        self.assertEqual(response.json["message"], "User added successfully")  

    def test_get_users(self):
        response = self.client.get('/users?page=1&limit=10')
        self.assertEqual(response.status_code, 200)
        # Check if the response contains the expected keys
        self.assertIn('data', response.get_json())
        self.assertIn('page', response.get_json())
        self.assertIn('limit', response.get_json())
        self.assertIn('total', response.get_json())
        self.assertIn('pages', response.get_json()) 

    def test_get_user(self):
        object_id = ObjectId()
        response = self.client.get(f'/users/{object_id}')
        self.assertEqual(response.status_code, 404)

    def test_delete_user(self):
        object_id = ObjectId()
        response = self.client.delete(f'/delete/{object_id}')
        self.assertEqual(response.status_code, 404)

    def test_update_user(self):
        object_id = ObjectId()
        data = {
            "name": "Test User Updated",
            "email": "testuser_updated@example.com",
            "password": "new_password"
        }
        response = self.client.put(f'/update/{object_id}', json=data) 
        self.assertEqual(response.status_code, 404)  

    def test_add_follower(self):
        object_id1 = ObjectId()
        object_id2 = ObjectId()
        data = {
            "user_id": f"{object_id1}",
            "follower_id": f"{object_id2}"
        }
        response = self.client.post('/follow', json=data)
        self.assertEqual(response.status_code, 404) 


if __name__ == '__main__':
    unittest.main()
