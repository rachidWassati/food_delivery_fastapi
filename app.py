from fastapi import Depends, FastAPI
from internal import admin
from models.database import get_db
from routers.api.v1 import restaurants

VERSION = 1

app = FastAPI(
    title= f"Food Delivery v{VERSION}",
    dependencies= [Depends(get_db)]
)


prefix_api = f"/api/v{VERSION}"

app.include_router(admin.router, prefix= prefix_api)
app.include_router(restaurants.router, prefix= prefix_api)