from sqlalchemy.orm import Session

from schemas.buyer import BuyerCreate
from db.models.buyer import Buyer

def create_new_buyer(buyer: BuyerCreate,db: Session):
    buyer = Buyer(
        phone_no=buyer.phone_no,
        email=buyer.email,
        actively_seeking=True
    )
    db.add(buyer)
    db.commit()
    db.refresh(buyer)
    return buyer
