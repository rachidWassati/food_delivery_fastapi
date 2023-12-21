from datetime import datetime, timedelta
from os import getenv
from typing import Optional, Type, TypeVar, Union
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer

from models.restaurant import Restaurant
from models.user import User
from schemas.token import TokenData
from utils.hashing import Hasher
from dotenv import load_dotenv

from jose import jwt, JWTError
load_dotenv()

ACCESS_TOKEN_EXPIRE_MINUTES= 60 * 24
ALGORITHM="HS256"
oauth_2_scheme = OAuth2PasswordBearer(tokenUrl="token")


T = TypeVar("T", bound= User)

def authenticate(document_type: Type[T], username: str, password: str) -> Union[bool, T]:
    user: T = document_type.objects(email=username).first()  # type: ignore
    if not user:
        return False
    if not Hasher.verify_password(password, user.password): # type: ignore
        return False
    return user

def generate_jwt_token(data: dict, expires_delta: Optional[timedelta] = None):
    to_encode = data.copy()
    expire = datetime.utcnow() + expires_delta if expires_delta else datetime.utcnow() + timedelta(minutes= ACCESS_TOKEN_EXPIRE_MINUTES)

    to_encode.update({"exp" : expire})
    return jwt.encode(to_encode, getenv("SECRET_KEY"), algorithm= ALGORITHM) # type: ignore

async def get_current_user(document_type: Type[T], token: str = Depends(oauth_2_scheme)):
    credential_exception = HTTPException(
            status_code= status.HTTP_401_UNAUTHORIZED, 
            detail= "Could not validate credentials",
            headers= {
                "WWW-Authenticate": "Bearer"
            }
            )
    try:
        payload = jwt.decode(token, getenv("SECRET_KEY"), algorithms= [ALGORITHM]) # type: ignore
        username : str = payload.get('sub') # type: ignore
        if username is None:
            raise credential_exception
        
        token_data = TokenData(username= username)
    except JWTError:
        return credential_exception
    
    return document_type.objects(email= username) # type: ignore

async def get_current_active_user(current_user: Restaurant= Depends(get_current_user)):
    if current_user.disabled:
        raise HTTPException(status_code= 400, detail= "Inactive user")
    return current_user  