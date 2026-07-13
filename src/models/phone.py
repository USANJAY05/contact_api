from src.core.db import Base
from sqlalchemy import Column, Integer, String, ForeignKey


class Phone(Base):
    __tablename__ = "phone"

    id = Column(Integer, primary_key=True, autoincrement=True)
    number = Column(String(20), nullable=False)
    contact_id = Column(Integer, ForeignKey("contact.id",ondelete="CASCADE"), nullable=False)