from fastapi import APIRouter, Depends

router = APIRouter(
    prefix= "/admin",
    tags= ["Admin"],
    # dependencies= [Depends()],
    responses= {404: {"description" : "Not found"}}
)


@router.get("/admin/restaurants/")
async def get_all_restaurants():
    return []

@router.post("/admin/restaurants/")
async def create_restaurant():
    return {"message": "New restaurant created"}