from fastapi import HTTPException

from src.core.db import session_local
from src.models.contact import Contact
from src.models.email import Email
from src.models.phone import Phone
from src.models.address import Address
from src.models.important_dates import ImportantDates
from src.models.website import Website
from src.models.work_info import WorkInfo
from src.models.contact_group import ContactGroup
from src.models.group import Group


def create_contact_service(data,user_id):
    try:
        with session_local() as session:

            payload = data.model_dump()

            # -----------------------------
            # Check for duplicate emails
            # -----------------------------
            # if payload.get("emails"):
            #     for email in payload["emails"]:
            #         existing_email = (
            #             session.query(Email)
            #             .filter(Email.email == email)
            #             .first()
            #         )

            #         if existing_email:
            #             raise HTTPException(
            #                 status_code=409,
            #                 detail={
            #                     "success": False,
            #                     "message": f"Email '{email}' already exists"
            #                 }
            #             )

            # -----------------------------
            # Check for Phone     
            # -----------------------------
            # if payload.get("phones"):
            #     for phone in payload["phones"]:
            #         existing_phone = (
            #             session.query(Phone)
            #             .filter(Phone.number == phone)
            #             .first()
            #         )

            #         if existing_phone:
            #             raise HTTPException(
            #                 status_code=409,
            #                 detail={
            #                     "success": False,
            #                     "message": f"Phone number '{phone}' already exists"
            #                 }
            #             )

            # -----------------------------
            # Check for group_id exist or not     
            # -----------------------------
            if payload.get("group_ids"):
                for group_id in payload["group_ids"]:
                    existing_group_id = (
                        session.query(Group)
                        .filter(Group.id == group_id)
                        .first()
                    )

                    if not existing_group_id:
                        raise HTTPException(
                            status_code=409,
                            detail={
                                "success": False,
                                "message": f"Group id '{group_id}' not exists"
                            }
                        )



            # -----------------------------
            # Create Contact
            # -----------------------------
            new_contact = Contact(
                user_id=user_id,
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


            # -----------------------------
            # Create Group
            # -----------------------------
            if payload.get("group_ids"):
                group_ids = [
                    ContactGroup(
                        contact_id=new_contact.id,
                        group_id=group_id
                    )
                    for group_id in payload["group_ids"]
                ]
                print(group_ids)
                session.add_all(group_ids)


            # -----------------------------
            # Create Work Info
            # -----------------------------
            if payload.get("work_info"):
                work_data = payload.get("work_info")
                print(work_data)
                work_info=WorkInfo(
                    **work_data,
                    contact_id=new_contact.id
                )
                session.add(work_info)


            # -----------------------------
            # Create Address
            # -----------------------------
            if payload.get("addresses"):
                address_info=[
                    Address(
                        **address_data,
                        contact_id=new_contact.id
                    )
                    for address_data in payload["addresses"]
                ]
                session.add_all(address_info)


            # -----------------------------
            # Create Website
            # -----------------------------
            if payload.get("websites"):
                Website_info=[
                    Website(
                        **Website_data,
                        contact_id=new_contact.id
                    )
                    for Website_data in payload["websites"]
                ]
                session.add_all(Website_info)


            # -----------------------------
            # Create important dates
            # -----------------------------
            if payload.get("important_dates"):
                important_dates_info=[
                    ImportantDates(
                        **important_dates_data,
                        contact_id=new_contact.id
                    )
                    for important_dates_data in payload["important_dates"]
                ]
                session.add_all(important_dates_info)


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