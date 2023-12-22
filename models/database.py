from dotenv import load_dotenv
from os import getenv
from mongoengine import connect, disconnect

load_dotenv()

def get_db_connection():
    try:
        db_connection = connect(
            host= getenv("MONGO_URI")
        )
        print("MONGO: ✅ Connection to Mongodb established !")
        yield db_connection
    finally:
        disconnect()
        print("MONGO: ⛔️ Disconnected from Mongodb!")