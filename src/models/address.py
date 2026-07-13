
from src.core.db import Base
from sqlalchemy import Integer, Column, String, ForeignKey

class Address(Base):
    __tablename__="address"
    id=Column(Integer,primary_key=True,autoincrement=True)
    street=Column(String(100))
    city=Column(String(100))
    state=Column(String(100))
    pincode=Column(Integer)
    country=Column(String(100))
    contact_id=Column(Integer,ForeignKey("contact.id",ondelete="CASCADE"),nullable=False)