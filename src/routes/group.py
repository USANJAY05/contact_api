from fastapi import APIRouter
from src.schema.group.request_schema import CreateGroupRequest
from src.services.group.create_group import create_group_service
from src.schema.group.response_schema import CreateGroupResponse
from src.services.group.delete_group import delete_group_service
from src.schema.group.response_schema import DeleteGroupResponse
from src.services.group.get_group import get_group_service
from src.schema.group.response_schema import GetAllGroupResponse
from src.services.group.update_group import update_group_service



route = APIRouter(
    prefix="/groups",
    tags=['GROUP']
)
user_id=1
@route.post("/",response_model=CreateGroupResponse)
def create_group(data: CreateGroupRequest):
    return create_group_service(data,user_id)


@route.get("/", response_model=GetAllGroupResponse)
def get_group():
    return get_group_service(user_id)


@route.put("/{group_id}", response_model=DeleteGroupResponse)
def update_group(group_id: int, data: CreateGroupRequest):
    return update_group_service(group_id, data,user_id)



@route.delete("/{group_id}", response_model=DeleteGroupResponse)
def delete_group(group_id: int):
    return delete_group_service(group_id,user_id)



