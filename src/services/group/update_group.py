from fastapi import HTTPException
from src.core.db import session_local
from src.models.group import Group
from src.schema.group.request_schema import CreateGroupRequest


def update_group_service(group_id: int, data: CreateGroupRequest):
    try:
        with session_local() as session:

            # Find the group by ID
            group = session.query(Group).filter(Group.id == group_id).first()

            # Check if group exists
            if not group:
                raise HTTPException(
                    status_code=404,
                    detail="Group not found"
                )

            # Update the group name
            group.name = data.name

            # Save changes
            session.commit()

            return {
                "success": True,
                "message": "Group updated successfully"
            }

    except HTTPException:
        raise

    except Exception as e:
        raise Exception(f"Failed to update group: {e}")