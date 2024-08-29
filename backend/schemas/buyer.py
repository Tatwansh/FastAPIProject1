from pydantic import BaseModel, EmailStr, Field


# Buyer Table constraints
class BuyerCreate(BaseModel):
    email: EmailStr
