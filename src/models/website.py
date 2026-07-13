from src.core.db import Base
from sqlalchemy import Column, Integer, String, ForeignKey


class Website(Base):
    __tablename__ = "website"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100), nullable=True)
    link = Column(String(500), nullable=False)
    contact_id = Column(Integer, ForeignKey("contact.id",ondelete="CASCADE"), nullable=False)