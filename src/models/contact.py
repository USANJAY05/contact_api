from src.core.db import Base
from sqlalchemy import Integer, Column, String, Text

class Contact(Base):
    __tablename__="contact"
    id=Column(Integer,primary_key=True,autoincrement=True)
    user_id=Column(Integer, nullable=False)
    first_name=Column(String(100),nullable=False)
    last_name=Column(String(100))
    relationship=Column(String(100))
    notes=Column(Text)