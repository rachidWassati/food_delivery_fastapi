from typing import List, Optional
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
    coverImages: Optional[List[str]] = None

class RestaurantUpdate(BaseModel):
    name: str
    ownerName: str
    foodTypes: List[str]
    postalcode: str
    address: str
    phone: str
    password: str
    coverImages: List[str]
