from pydantic import BaseModel, EmailStr, Field


#Adding Constraints to Seller
class SellerCreate(BaseModel):
    email: EmailStr
