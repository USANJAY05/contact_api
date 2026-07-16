from fastapi import HTTPException

from src.core.db import session_local
from src.models.contact import Contact


def delete_contact_service(contact_id: int, user_id):
    try:
        with session_local() as session:

            contact = (
                session.query(Contact)
                .filter(Contact.id == contact_id, Contact.user_id==user_id)
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

            session.delete(contact)

            session.commit()

            return {
                "success": True,
                "message": "Contact deleted successfully"
            }

    except HTTPException:
        raise

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=str(e)
        )