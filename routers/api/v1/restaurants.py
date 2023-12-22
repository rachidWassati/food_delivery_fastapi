from fastapi import APIRouter, Body, Depends, HTTPException, Request
from fastapi.security import HTTPAuthorizationCredentials
import mongoengine
from auth.jwt_bearer import JwtBearer
from auth.jwt_handler import check_user, get_current_user, signJWT

from models.restaurant import Restaurant
from schemas.restaurant import RestaurantBase, RestaurantCreate, RestaurantResponse
from schemas.user import UserLoginSchema
from utils.hashing import Hasher

router = APIRouter(
    prefix= "/restaurant",
    tags= ["Restaurant"],
    # dependencies= [Depends()],
    responses= {404: {"description" : "Not found"}}
)

security = JwtBearer()

@router.post("/register")
async def register(restaurant: RestaurantBase = Body(default= None)):
    try:
        new_restaurant = Restaurant(**restaurant.dict())
        new_restaurant.password = Hasher.get_password_hash(restaurant.password)
        new_restaurant.save()
        return signJWT(restaurant.email)
    except mongoengine.errors.NotUniqueError:
        return HTTPException(409, detail= f"Restaurant already registered with email: {restaurant.email}")
    
@router.post('/login')
async def login(restaurant: UserLoginSchema = Body(default= None)):
    if check_user(model= Restaurant, data= restaurant):
        return signJWT(restaurant.email)
    else:
        return {"error", "Invalid login details"}

@router.get('/profile')
async def show_profile(token: HTTPAuthorizationCredentials= Depends(security)):
    restaurant = get_current_user(model= Restaurant, token= token) # type: ignore
    return restaurant.to_dict()