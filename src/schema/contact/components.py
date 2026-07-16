from pydantic import BaseModel
from datetime import date

class WorkInfo(BaseModel):
    job_name: str
    department: str
    company: str

class Address(BaseModel):
    category: str
    street: str
    city: str
    state: str
    pincode: int
    country: str

class Website(BaseModel):
    name: str
    link: str

class ImportantDate(BaseModel):
    name: str
    date: date
