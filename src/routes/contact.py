from fastapi import APIRouter
from fastapi import Query

from src.schema.contact.request_schema import CreateContactRequest
from src.schema.contact.response_schema import CreateContactResponse
from src.services.contact.create_contact import create_contact_service
from src.services.contact.get_contact import get_contact_service
from src.schema.contact.response_schema import GetAllContactResponse
from src.services.contact.get_contact_by_id import get_contact_by_id_service
from src.schema.contact.response_schema import GetContactByIdResponse
from src.services.contact.get_contact import get_contact_service
from src.schema.contact.response_schema import GetAllContactResponse
from src.services.contact.get_contact_by_id import get_contact_by_id_service
from src.schema.contact.response_schema import GetContactByIdResponse
from src.services.contact.update_contact import update_contact_service
from src.schema.contact.response_schema import UpdateContactResponse
from src.services.contact.delete_contact import delete_contact_service
from src.schema.contact.response_schema import DeleteContactResponse



route = APIRouter(
    prefix="/contacts",
    tags=['CONTACT']
)

@route.post("/", response_model=CreateContactResponse, status_code=201)
def create_contact(data: CreateContactRequest):
    return create_contact_service(data)



@route.get("/", response_model=GetAllContactResponse)
def get_contacts(
    page: int = Query(1, ge=1),
    limit: int = Query(10, ge=1)
):
    return get_contact_service(page, limit)


@route.get("/{contact_id}", response_model=GetContactByIdResponse)
def get_contact_by_id(contact_id: int):
    return get_contact_by_id_service(contact_id)


@route.put("/{contact_id}", response_model=UpdateContactResponse)
def update_contact(contact_id: int, data: CreateContactRequest):
    return update_contact_service(contact_id, data)


@route.delete("/{contact_id}", response_model=DeleteContactResponse)
def delete_contact(contact_id: int):
    return delete_contact_service(contact_id)


@route.get("/search")
def search_contact(data: CreateContactRequest):
    return data
