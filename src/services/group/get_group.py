from src.core.db import session_local
from src.models.group import Group


def get_group_service():
    try:
        with session_local() as session:

            groups = session.query(Group).all()

            return {
                "success": True,
                "data": groups
            }

    except Exception as e:
        raise Exception(f"Failed to get groups: {e}")