from sqlalchemy.orm import Session

from schemas.seller import SellerCreate
from db.models.seller import Seller

def create_new_seller(seller: SellerCreate,db: Session):
    buyer = Seller(
        name=seller.name,
        phone_no=seller.phone_no,
        e_mail=seller.e_mail,
        actively_seeking=True
    )
    db.add(buyer)
    db.commit()
    db.refresh(buyer)
    return buyer
