from fastapi import HTTPException
from src.models.email import Email
from src.models.phone import Phone
from src.core.db import session_local
from src.models.contact import Contact
from src.schema.contact.request_schema import CreateContactRequest


def update_contact_service(contact_id: int, data: CreateContactRequest):

    try:
        with session_local() as session:

            contact = (
                session.query(Contact)
                .filter(Contact.id == contact_id)
                .first()
            )

            if not contact:
                raise HTTPException(
                    status_code=404,
                    detail={
                        "success": False,
                        "message": "Contact not found"
                    }
                )

            payload = data.model_dump()

            contact.first_name = payload["first_name"]
            contact.last_name = payload["last_name"]
            contact.relationship = payload["relationship"]
            contact.notes = payload["notes"]

            # Delete existing emails
            session.query(Email).filter(
                Email.contact_id == contact_id
            ).delete()

            # Add new emails
            if payload.get("emails"):
                new_emails = [
                    Email(
                        contact_id=contact_id,
                        email=email
                    )
                    for email in payload["emails"]
                ]

                session.add_all(new_emails)

            # Delete existing phones
            session.query(Phone).filter(
                Phone.contact_id == contact_id
            ).delete()

            # Add new phones
            if payload.get("phones"):
                new_phones = [
                    Phone(
                        contact_id=contact_id,
                        number=phone
                    )
                    for phone in payload["phones"]
                ]

                session.add_all(new_phones)

            session.commit()

            return {
                "success": True,
                "message": "Contact updated successfully"
            }

    except HTTPException:
        raise

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Failed to update contact: {e}"
        )