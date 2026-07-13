from fastapi import HTTPException

from src.core.db import session_local
from src.models.contact import Contact
from src.models.email import Email
from src.models.phone import Phone


def get_contact_by_id_service(contact_id: int):

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

            emails = (
                session.query(Email)
                .filter(Email.contact_id == contact_id)
                .all()
            )

            phones = (
                session.query(Phone)
                .filter(Phone.contact_id == contact_id)
                .all()
            )

            return {
                "success": True,
                "data": {
                    "id": contact.id,
                    "first_name": contact.first_name,
                    "last_name": contact.last_name,
                    "relationship": contact.relationship,
                    "notes": contact.notes,
                    "emails": emails,
                    "phones": phones
                }
            }

    except HTTPException:
        raise

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Failed to get contact: {e}"
        )