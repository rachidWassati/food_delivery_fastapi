from datetime import timedelta
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from auth.oauth2 import ACCESS_TOKEN_EXPIRE_MINUTES, generate_jwt_token, authenticate
from models.restaurant import Restaurant

from schemas.token import Token

router = APIRouter(
    tags= ["Authentication"],
    responses= {404: {"description" : "Not found"}}
)

@router.post('/token', response_model=Token)
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
    user : Restaurant | bool = authenticate(Restaurant, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED, 
                detail="Incorrect username or password",
                headers= {"WWW-Authenticate" : "Bearer"}
                )
    access_token_expires = timedelta(minutes= ACCESS_TOKEN_EXPIRE_MINUTES)
    acces_token = generate_jwt_token(
        data= {"sub": user.email}, # type: ignore
        expires_delta= access_token_expires
    )
    return {"access_token": acces_token, "token_type": "bearer"}
