from pydantic import BaseModel, EmailStr, Field


#Adding Constraints to Seller
class SellerCreate(BaseModel):
    email: EmailStr
    phone_no = Field(gt=999999999, lt=1000000000)
