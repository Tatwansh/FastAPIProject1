from fastapi import APIRouter
from apiS.ver1 import route_buyer, route_seller

api_router = APIRouter()
api_router.include_router(router=route_buyer.router, prefix='', tags=['buyers'])
api_router.include_router(router=route_seller.router, prefix='', tags=['sellers'])
