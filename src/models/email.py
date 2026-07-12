from src.core.db import Base
from sqlalchemy import Integer, Column, String, ForeignKey

class Email(Base):
    __tablename__="email"
    id=Column(Integer,primary_key=True,autoincrement=True)
    email=Column(String(255),nullable=False)
    contact_id=Column(Integer,ForeignKey("contact.id"),nullable=False)