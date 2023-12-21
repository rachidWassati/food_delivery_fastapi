from dotenv import load_dotenv
from os import getenv
from mongoengine import connect

from models.restaurant import Restaurant

load_dotenv()

def get_db_connection():
    db_connection = connect(
        host= getenv("MONGO_URI")
    )
    print("MONGO: ✅ Connection to Mongodb established !")
    return db_connection

# new_restau = {
#     "name": "Le Petit Bistro",
#     "ownerName": "Isabelle Dupont",
#     "foodTypes": ["French", "Seafood"],
#     "postalcode": "75001",
#     "address": "10 Rue de la Roquette",
#     "phone": "01 45 67 89 10",
#     "email": "lepetitbistro@gmail.com",
#     "password": "qwerty"
# }

# restaurant = Restaurant(**new_restau)
# restaurant.save()