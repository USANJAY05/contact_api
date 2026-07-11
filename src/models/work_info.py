from src.core.db import Base
from sqlalchemy import Column, Integer, String, ForeignKey


class WorkInfo(Base):
    __tablename__ = "work_info"

    id = Column(Integer, primary_key=True, autoincrement=True)
    job_name = Column(String(150), nullable=True)
    department = Column(String(100), nullable=True)
    company = Column(String(150), nullable=True)
    contact_id = Column(Integer, ForeignKey("contact.id"), nullable=False)