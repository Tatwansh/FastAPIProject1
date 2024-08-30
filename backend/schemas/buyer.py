from pydantic import BaseModel, EmailStr, Field


# Buyer Table constraints
class BuyerCreate(BaseModel):
    name: str = Field(..., min_length=1)
    e_mail: EmailStr
    phone_no: int = Field(..., gt=999999999, le=9999999999)


class ShowBuyer(BaseModel):
    id: int
    name: str
    phone_no: int
    actively_seeking: bool

    class Config():
        orm_mode = True
