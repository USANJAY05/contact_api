from src.core.db import Base
from sqlalchemy import Column, Integer, String, Date, ForeignKey


class ImportantDates(Base):
    __tablename__ = "important_dates"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100), nullable=False)
    date = Column(Date, nullable=False)
    contact_id = Column(Integer, ForeignKey("contact.id"), nullable=False)