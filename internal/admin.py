from fastapi import APIRouter, HTTPException
from fastapi.responses import JSONResponse
import mongoengine
from models.restaurant import Restaurant
from schemas.restaurant import RestaurantCreate
from utils.hashing import Hasher

router = APIRouter(
    prefix= "/admin",
    tags= ["Admin"],
    # dependencies= [Depends()],
    responses= {404: {"description" : "Not found"}}
)

@router.get("/restaurants/")
async def get_all_restaurants():
    # Convertir le QuerySet en une liste de dictionnaires
    restaurants_data = [restaurant.to_dict() for restaurant in Restaurant.objects()] # type: ignore

    # Retourner la liste de dictionnaires en tant que réponse JSON
    return JSONResponse(content=restaurants_data)

@router.post("/restaurants/")
async def create_restaurant(restaurant: RestaurantCreate):
    try:
        new_restaurant = Restaurant(**restaurant.dict())
        # on ecrase la valeur de `password` avec son hashage
        new_restaurant.password = Hasher.get_password_hash(restaurant.password)
        restaurant_created = new_restaurant.save()
        
        return {"status": "success", "restaurant": restaurant_created.to_dict()}
    except mongoengine.errors.NotUniqueError:
        return HTTPException(409, detail= f"Restaurant already registered with email: {restaurant.email}")