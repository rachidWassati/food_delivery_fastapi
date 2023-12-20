from pymongo import MongoClient
from dotenv import load_dotenv
from os import getenv

load_dotenv()

def get_db():
    client = MongoClient(getenv("MONGO_URI"))
    try:
        print("MONGO: ✅ Connection to Mongodb established !")
        yield client
    finally:
        client.close()