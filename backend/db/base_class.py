from typing import Any
from sqlalchemy.ext.declarative import declared_attr
from sqlalchemy.orm import as_declarative

@as_declarative()
class BASE:
    id: Any
    name: Any
    phone_no: Any
    e_mail: Any
    __name__: str


    @declared_attr
    def __tablename__(cls):
        return cls.__name__.capitalize()