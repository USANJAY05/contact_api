from pydantic import BaseModel
from typing import Optional

class Address(BaseModel):
    id: int
    street: Optional[str]=None
    city: Optional[str]=None
    state: Optional[str]=None
    pincode: Optional[int]=None
    country: Optional[str]=None
    contact_id: int

class ContactGroup(BaseModel):
    group_id: int
    contact_id: int