from db.base_class import BASE
from sqlalchemy import String, Integer, Column, Boolean, Date
from datetime import date


# Buyer table definitions
class Buyer(BASE):
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    phone_no = Column(Integer, nullable=False)
    e_mail = Column(String)
    seeking_since = Column(Date, default=date.today())
    actively_seeking = Column(Boolean, default=True)
