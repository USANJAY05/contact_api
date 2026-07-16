from src.core.db import session_local
from src.models.group import Group
from fastapi import HTTPException

def delete_group_service(group_id: int, user_id):
    try:
        with session_local() as session:

            # Find the group by ID
            group = session.query(Group).filter(Group.id==group_id, Group.user_id==user_id).first()
            print(group)
            print("HIHIHIHIHIHIHIHIH")

            # Check if the group exists
            if group is None:
                raise HTTPException(
                    status_code=404,
                    detail="Group not found"
                )
            # Delete the group
            session.delete(group)
            print('ttefafasdafa')

            # Save changes
            session.commit()

            # Return success message
            return {
                        "success": True,
                        "message": "Group deleted successfully"
                    }

    except HTTPException:
        raise

    except Exception as e:
        raise Exception(f"Failed to delete group: {e}")