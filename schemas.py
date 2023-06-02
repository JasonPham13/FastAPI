from pydantic import BaseModel
from typing import Optional


class UserModel (BaseModel):

    id:int
    username: str
    email: str
    role: str

    class Config:

        orm_mode = True


class CreateUserModel(BaseModel):
    username: str
    email: str
    role: str

class UpdateUserModel(BaseModel):
    email: Optional[str]
    role: Optional[str]


class MessageModel(BaseModel):
    detail: str
