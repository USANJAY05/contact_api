from pydantic import BaseModel
from typing import Optional

class CreateGroupRequest(BaseModel):
    name: str

