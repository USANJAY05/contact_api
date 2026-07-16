from pydantic import BaseModel, EmailStr
from typing import Optional
from src.schema.contact.components import WorkInfo, Address, Website, ImportantDate



class CreateContactRequest(BaseModel):
    first_name: str
    last_name: Optional[str]=None
    relationship: Optional[str]=None
    notes: Optional[str]=None
    emails: Optional[list[EmailStr]]=None
    phones: list[str]
    group_ids: Optional[list[int]]=None
    work_info: Optional[WorkInfo]=None
    addresses: Optional[list[Address]]=None
    websites: Optional[list[Website]]=None
    important_dates: Optional[list[ImportantDate]]=None


class SearchQuery(BaseModel):
    page: Optional[int]=1
    limit: Optional[int]=10
    name: Optional[str]=None
    phone: Optional[str]=None
    email: Optional[str]=None
