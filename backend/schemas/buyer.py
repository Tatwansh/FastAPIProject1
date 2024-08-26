from pydantic import BaseModel, EmailStr, Field


# Buyer Table constraints
class BuyerCreate(BaseModel):
    email: EmailStr
    phone_no = Field(gt=999999999, lt=1000000000)
