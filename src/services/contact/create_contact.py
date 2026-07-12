from src.core.db import session_local
from src.models.contact import Contact
from src.models.email import Email
from src.models.phone import Phone
from src.models.group import Group

def create_contact_service(data):
    try:
        with session_local() as session:
            payload = data.model_dump()

            contact_data = {
                "first_name": payload["first_name"],
                "last_name": payload["last_name"],
                "relationship": payload["relationship"],
                "notes": payload["notes"],
            }

            new_contact = Contact(**contact_data)

            session.add(new_contact)
            session.flush()  # populates new_contact.id

            new_emails = [
                Email(
                    contact_id=new_contact.id,
                    email=email_address
                )
                for email_address in payload["emails"]
            ]

            session.add_all(new_emails)




            new_phones = [
                Phone(
                    contact_id=new_contact.id,
                    number=phone_number
                )
                for phone_number in payload["phones"]
            ]

            session.add_all(new_phones)
            print("grooooouup")
            print(data)

            group_data={
                "name":payload.get("name")
            }
            new_group=Group(**group_data)
            session.add(new_group)
            session.commit

            

            return new_contact

    except Exception as e:
        raise Exception(f"Failed to create contact: {e}")