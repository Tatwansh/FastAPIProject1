from fastapi import APIRouter
from sqlalchemy.orm import Session
from fastapi import Depends

from schemas.buyer import BuyerCreate
from db.session import get_db
from db.repository.buyer import create_new_buyer

router = APIRouter()


@router.post("/")
def create_buyer(buyer: BuyerCreate, db: Session = Depends(get_db)):
    buyer = create_new_buyer(buyer=buyer, db=db)
    return buyer
