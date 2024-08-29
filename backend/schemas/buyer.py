from pydantic import BaseModel, EmailStr, Field


# Buyer Table constraints
class BuyerCreate(BaseModel):
    e_mail: EmailStr
    phone_no: int = Field(..., gt=999999999, le=9999999999)
