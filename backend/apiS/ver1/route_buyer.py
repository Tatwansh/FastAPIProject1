from fastapi import APIRouter, status
from sqlalchemy.orm import Session
from fastapi import Depends

from schemas.buyer import BuyerCreate, ShowBuyer
from db.session import get_db
from db.repository.buyer import create_new_buyer

router = APIRouter()


@router.post("/buyers", response_model=ShowBuyer, status_code=status.HTTP_201_CREATED)
def create_buyer(buyer: BuyerCreate, db: Session = Depends(get_db)):
    buyer = create_new_buyer(buyer=buyer, db=db)
    return buyer
