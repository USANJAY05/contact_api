from fastapi import APIRouter
from fastapi import Request
from src.schema.contact import CreateContactRequest, CreateContactResponse
from src.services.contact.create_contact import create_contact_service

route = APIRouter(
    prefix="/contacts",
    tags=['CONTACT']
)

@route.post("/")
def create_contact(data: CreateContactRequest):
    create_contact_service(data)
    return data

@route.get("/")
def get_contact(data: CreateContactRequest):
    return data


@route.get("/{id}")
def get_contact_by_id(data: CreateContactRequest):
    return data


@route.put("/{id}")
def update_contact(data: CreateContactRequest):
    return data


@route.delete("/{id}")
def delete_contact(data: CreateContactRequest):
    return data


@route.get("/search")
def search_contact(data: CreateContactRequest):
    return data
