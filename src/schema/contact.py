from pydantic import BaseModel, EmailStr
from typing import Optional


class WorkInfo(BaseModel):
    job_name: str
    department: str
    company: str

class Address(BaseModel):
    street: str
    city: str
    state: str
    pincode: str
    country: str

class Website(BaseModel):
    name: str
    link: str

class ImportantDate(BaseModel):
    name: str
    date: str

class CreateContactRequest(BaseModel):
    first_name: str
    last_name: Optional[str]=None
    relationship: Optional[str]=None
    notes: Optional[str]=None
    emails: Optional[list[EmailStr]]=None
    phones: list[str]
    group_ids: Optional[list[int]]=None
    work_info: Optional[WorkInfo]=None
    addresses: Optional[Address]=None
    websites: Optional[Website]=None
    important_dates: Optional[ImportantDate]=None





class CreateContactResponse(BaseModel):
    success: bool
    message: str
    data: dict