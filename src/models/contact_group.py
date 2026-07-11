
from src.core.db import Base
from sqlalchemy import Integer, Column, String, ForeignKey

class ContactGroup(Base):
    __tablename__="contact_group"
    group_id=Column(Integer,ForeignKey("group.id"),primary_key=True)
    contact_id=Column(Integer,ForeignKey("contact.id"),primary_key=True)