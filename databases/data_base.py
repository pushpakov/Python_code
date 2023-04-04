from pymongo import MongoClient
from dotenv import load_dotenv
import os

# load environment variables from .env file
load_dotenv()

# get environment variables
MONGODB_URI = os.getenv('MONGODB_URI')
DB_NAME = os.getenv('DB_NAME')
COLLECTION_NAME = os.getenv('COLLECTION_NAME')

class Database:
    def __init__(self, MONGODB_URI, DB_NAME):
        self.client = MongoClient(MONGODB_URI) 
        self.db = self.client[DB_NAME] 

    def get_collection(self, COLLECTION_NAME):
        return self.db[COLLECTION_NAME] 
    



