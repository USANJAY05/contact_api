from pydantic import BaseModel

class CreateContactResponse(BaseModel):
    success: bool
    message: str
    data: dict