from sqlalchemy.orm import Session

from schemas.buyer import BuyerCreate
from db.models.buyer import Buyer

def create_new_buyer(buyer: BuyerCreate,db: Session):
    buyer = Buyer(
        name=buyer.name,
        phone_no=buyer.phone_no,
        e_mail=buyer.e_mail,
        actively_seeking=True
    )
    db.add(buyer)
    db.commit()
    db.refresh(buyer)
    return buyer
