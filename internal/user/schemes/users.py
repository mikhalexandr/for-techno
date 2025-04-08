from pydantic import BaseModel, EmailStr


class UserRegisterRq(BaseModel):
    id: str
    userName: str
    email: EmailStr


class UserRegisterRs(BaseModel):
    status: str
