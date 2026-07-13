from fastapi import HTTPException

from src.core.db import session_local
from src.models.contact import Contact
from src.models.email import Email
from src.models.phone import Phone


def create_contact_service(data):
    try:
        with session_local() as session:

            payload = data.model_dump()

            # -----------------------------
            # Check for duplicate emails
            # -----------------------------
            if payload.get("emails"):
                for email in payload["emails"]:
                    existing_email = (
                        session.query(Email)
                        .filter(Email.email == email)
                        .first()
                    )

                    if existing_email:
                        raise HTTPException(
                            status_code=409,
                            detail={
                                "success": False,
                                "message": f"Email '{email}' already exists"
                            }
                        )

            # -----------------------------
            # Check for duplicate phone numbers
            # -----------------------------
            if payload.get("phones"):
                for phone in payload["phones"]:
                    existing_phone = (
                        session.query(Phone)
                        .filter(Phone.number == phone)
                        .first()
                    )

                    if existing_phone:
                        raise HTTPException(
                            status_code=409,
                            detail={
                                "success": False,
                                "message": f"Phone number '{phone}' already exists"
                            }
                        )

            # -----------------------------
            # Create Contact
            # -----------------------------
            new_contact = Contact(
                first_name=payload["first_name"],
                last_name=payload.get("last_name"),
                relationship=payload.get("relationship"),
                notes=payload.get("notes")
            )

            session.add(new_contact)
            session.flush()

            # -----------------------------
            # Create Emails
            # -----------------------------
            if payload.get("emails"):
                emails = [
                    Email(
                        contact_id=new_contact.id,
                        email=email
                    )
                    for email in payload["emails"]
                ]
                session.add_all(emails)

            # -----------------------------
            # Create Phones
            # -----------------------------
            if payload.get("phones"):
                phones = [
                    Phone(
                        contact_id=new_contact.id,
                        number=phone
                    )
                    for phone in payload["phones"]
                ]
                session.add_all(phones)

            session.commit()
            session.refresh(new_contact)

            return {
                "success": True,
                "message": "Contact created successfully",
                "data": {
                    "contact_id": new_contact.id
                }
            }

    except HTTPException:
        raise

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail={
                "success": False,
                "message": f"Failed to create contact: {str(e)}"
            }
        )