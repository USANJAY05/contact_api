from math import ceil

from src.core.db import session_local
from src.models.contact import Contact


def get_contact_service(page: int, limit: int, user_id):

    try:
        with session_local() as session:

            # Total records
            total_records = session.query(Contact).filter(Contact.user_id==user_id).count()

            # Total pages
            total_pages = ceil(total_records / limit) if total_records > 0 else 1

            # Pagination
            contacts = (
                session.query(Contact)
                .filter(Contact.user_id==user_id)
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
                    "total_pages": total_pages
                }
            }

    except Exception as e:
        raise Exception(f"Failed to get contacts: {e}")