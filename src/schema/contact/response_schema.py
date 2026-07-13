from pydantic import BaseModel

class ContactId(BaseModel):
    contact_id: int


class CreateContactResponse(BaseModel):
    success: bool
    message: str
    data: ContactId


class ContactData(BaseModel):
    id: int
    first_name: str
    last_name: str | None = None
    relationship: str | None = None


class Pagination(BaseModel):
    page: int
    limit: int
    total_records: int
    total_pages: int


class GetAllContactResponse(BaseModel):
    success: bool
    data: list[ContactData]
    pagination: Pagination


class EmailResponse(BaseModel):
    id: int
    email: str


class PhoneResponse(BaseModel):
    id: int
    number: str


class ContactData(BaseModel):
    id: int
    first_name: str
    last_name: str | None = None
    relationship: str | None = None
    notes: str | None = None

    emails: list[EmailResponse]
    phones: list[PhoneResponse]


class GetContactByIdResponse(BaseModel):
    success: bool
    data: ContactData



class UpdateContactResponse(BaseModel):
    success: bool
    message: str


class DeleteContactResponse(BaseModel):
    success: bool
    message: str