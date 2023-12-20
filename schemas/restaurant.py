from typing import List
from pydantic import BaseModel


class RestaurantBase(BaseModel):
    name: str
    ownerName: str
    foodTypes: List[str]
    postalcode: str
    address: str
    phone: str
    email: str
    password: str
    serviceAvailable: bool
    coverImages: List[str]
    rating: float

class RestaurantCreate(BaseModel):
    name: str
    ownerName: str
    foodTypes: List[str]
    postalcode: str
    address: str
    phone: str
    email: str
    password: str
    coverImages: List[str]

class RestaurantUpdate(BaseModel):
    name: str
    ownerName: str
    foodTypes: List[str]
    postalcode: str
    address: str
    phone: str
    password: str
    coverImages: List[str]
