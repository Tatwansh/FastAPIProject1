from sqlalchemy.orm import Session

from schemas.seller import SellerCreate
from db.models.seller import Seller

def create_new_seller(seller: SellerCreate,db: Session):
    seller = Seller(
        name=seller.name,
        phone_no=seller.phone_no,
        e_mail=seller.e_mail,
        Plot_Add=seller.Plot_Add,
        Plot_Details=seller.Plot_Details,
        Expected_Price=seller.Expected_Price,
        actively_seeking=True
    )
    db.add(seller)
    db.commit()
    db.refresh(seller)
    return seller
