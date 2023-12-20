from fastapi import FastAPI
from internal import admin
from routers.api.v1 import restaurants


app = FastAPI()

VERSION = 1

prefix_api = f"/api/v{VERSION}"

app.include_router(admin.router, prefix= prefix_api, tags= [f"v{VERSION}"])
app.include_router(restaurants.router, prefix= prefix_api, tags= [f"v{VERSION}"])