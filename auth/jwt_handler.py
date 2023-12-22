from time import time
from typing import Type, TypeVar
from dotenv import load_dotenv
from fastapi import HTTPException
import jwt
from os import getenv
from models.user import User

from schemas.user import UserLoginSchema
from utils.hashing import Hasher

load_dotenv()

JWT_SECRET = getenv("SECRET_KEY")
JWT_ALGORITHM = getenv("ALGORITHM")

def token_response(token: str):
    return {"access token" : token}

def signJWT(email: str):
    payload = {
        "username" : email,
        "expiry": time() + 600
    }

    token = jwt.encode(payload, JWT_SECRET, algorithm=JWT_ALGORITHM) # type: ignore
    return token_response(token)

def decodeJWT(token: str) -> dict:
    try:
        decode_token = jwt.decode(token, key= JWT_SECRET, algorithms=[JWT_ALGORITHM]) # type: ignore
        return decode_token if decode_token['expiry'] >= time() else {}
    except:
        return {}
    
T = TypeVar("T", bound= User)
    
def check_user(model: Type[T], data: UserLoginSchema):
    user : T = model.objects(email= data.email).first() # type: ignore
    if user is None:
        raise HTTPException(404, detail= "No User found")
    if not Hasher.verify_password(data.password, user.password):
        raise HTTPException(404, detail= "Email or Password are wrong")
    return True

def get_current_user(model: Type[T], token: str) -> T:
    decoded_data = decodeJWT(token)
    email: str = decoded_data['username']
    user : T = model.objects(email= email).first() # type: ignore
    if user is None:
        raise HTTPException(404, detail= "No User found")
    return user # type: ignore