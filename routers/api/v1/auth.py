from fastapi import APIRouter, Depends, HTTPException, status

from auth.jwt_handler import check_user

router = APIRouter(
    tags= ["Authentication"],
    responses= {404: {"description" : "Not found"}}
)


