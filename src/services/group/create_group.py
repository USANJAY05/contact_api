from src.core.db import session_local
from src.models.group import Group
from sqlalchemy.exc import IntegrityError
from fastapi.exceptions import HTTPException

def create_group_service(data):
    try:
        with session_local() as session:
            new_group = Group(**data.model_dump())

            session.add(new_group)
            # session.flush() 
            session.commit()
            session.refresh(new_group)
            print(new_group.id)
            print(new_group)

            return new_group

    except IntegrityError as e:
        raise HTTPException(status_code=400, detail="Calendar already exists")


    
    except Exception as e:
        raise Exception(f"Failed to create group:{e}")
