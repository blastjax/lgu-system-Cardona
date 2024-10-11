from fastapi import APIRouter, Response

# from app.queries import *

router = APIRouter()


@router.get("/ping")
async def root():
    return {"message": "Hello World"}
