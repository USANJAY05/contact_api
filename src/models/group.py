# from src.core.db import Base
# from sqlalchemy import Integer, Column, String, ForeignKey

# class Group(Base):
#     __tablename__="group"
#     id=Column(Integer,primary_key=True,autoincrement=True)
#     user_id=Column(Integer,nullable=False)
#     name=Column(String(100),nullable=False)


from sqlalchemy import Column, Integer, String, UniqueConstraint
from src.core.db import Base

class Group(Base):
    __tablename__ = "group"

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, nullable=False)
    name = Column(String(100), nullable=False)

    __table_args__ = (
        UniqueConstraint("user_id", "name", name="uq_group_user_name"),
    )