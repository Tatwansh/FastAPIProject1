from pydantic import BaseModel, EmailStr, Field


#Adding Constraints to Seller
class SellerCreate(BaseModel):
    name: str = Field(..., min_length=1)
    e_mail: EmailStr
    phone_no: int = Field(..., gt=999999999, le=9999999999)
    Plot_Add: str = Field(..., min_length=1)
    Plot_Details: Optional[str]
    Expected_price: int = Field(..., ge=0)


class ShowSeller(BaseModel):
    id: int
    name: str
    phone_no: int
    Plot_Add: str
    actively_seeking: bool

    class Config():
        orm_mode = True
