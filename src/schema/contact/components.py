from pydantic import BaseModel

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
