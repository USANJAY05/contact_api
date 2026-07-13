from pydantic import BaseModel

class CreateGroupResponse(BaseModel):
    success: bool
    message: str


class GroupData(BaseModel):
    id: int
    name: str


class GetAllGroupResponse(BaseModel):
    success: bool
    data: list[GroupData]


class DeleteGroupResponse(BaseModel):
    success: bool
    message: str

