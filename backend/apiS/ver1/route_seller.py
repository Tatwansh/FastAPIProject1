from fastapi import APIRouter, status
from sqlalchemy.orm import Session
from fastapi import Depends

from schemas.seller import SellerCreate, ShowSeller
from db.session import get_db
from db.repository.seller import create_new_seller

router = APIRouter()


@router.post("/sellers", response_model=ShowSeller, status_code=status.HTTP_201_CREATED)
async def create_buyer(buyer: SellerCreate, db: Session = Depends(get_db)):
    seller = create_new_seller(seller=seller, db=db)
    return seller
