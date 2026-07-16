from math import ceil
from sqlalchemy import or_

from src.core.db import session_local
from src.models.contact import Contact
from src.models.phone import Phone
from src.models.email import Email


def search_contact_service(query, user_id):

    page = query.page
    limit = query.limit

    try:
        with session_local() as session:

            db_query = (
                session.query(Contact)
                .outerjoin(Phone, Phone.contact_id == Contact.id)
                .outerjoin(Email, Email.contact_id == Contact.id)
                .filter(Contact.user_id == user_id)
            )

            if query.name:
                db_query = db_query.filter(
                    Contact.first_name.ilike(f"%{query.name}%")
                )

            if query.phone:
                db_query = db_query.filter(
                    Phone.number.ilike(f"%{query.phone}%")
                )

            if query.email:
                db_query = db_query.filter(
                    Email.email.ilike(f"%{query.email}%")
                )

            total_records = db_query.distinct(Contact.id).count()

            total_pages = (
                ceil(total_records / limit)
                if total_records > 0
                else 1
            )

            contacts = (
                db_query
                .distinct(Contact.id)
                .offset((page - 1) * limit)
                .limit(limit)
                .all()
            )

            return {
                "success": True,
                "data": contacts,
                "pagination": {
                    "page": page,
                    "limit": limit,
                    "total_records": total_records,
                    "total_pages": total_pages,
                },
            }

    except Exception as e:
        raise Exception(f"Failed to search contacts: {e}")