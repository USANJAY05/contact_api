from src.core.db import Base
from sqlalchemy import Integer, Column, String, ForeignKey

class Group(Base):
    __tablename__="group"
    id=Column(Integer,primary_key=True,autoincrement=True)
    name=Column(String(100),unique=True,nullable=False)
