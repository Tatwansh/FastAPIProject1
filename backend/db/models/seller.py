from db.base_class import BASE
from sqlalchemy import Column, Integer, Boolean, String, Text, Date
from sqlalchemy.orm import relationship
from datetime import date


# Seller Table Definitions
class Seller(BASE):
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    phone_no = Column(Integer, nullable=False)
    e_mail = Column(String)
    Plot_Add = Column(Text, unique=True)
    Expected_Price = Column(Integer, default=0)
    Plot_Details = Column(Text, nullable=False)
    seeking_from = Column(Date, default=date.today())
    actively_seeking = Column(Boolean, default=True)
