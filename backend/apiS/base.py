from fastapi import APIRouter
from apiS.ver1 import route_buyer

api_router = APIRouter()
api_router.include_router(router=route_buyer.router, prefix='', tags=['buyers'])
