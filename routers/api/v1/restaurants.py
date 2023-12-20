from fastapi import APIRouter, Depends

router = APIRouter(
    prefix= "/restaurant",
    tags= ["Restaurant"],
    # dependencies= [Depends()],
    responses= {404: {"description" : "Not found"}}
)


@router.get("/")
async def get_all_restaurants():
    return []

@router.post("/")
async def create_restaurant():
    return {"message": "New restaurant created"}