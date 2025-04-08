from pydantic import BaseModel, EmailStr


class SuperadminRs(BaseModel):
    status: str


class SuperadminUpdateRq(BaseModel):
    id: str
    email: EmailStr


class SuperadminCreateRq(SuperadminUpdateRq):
    userName: str
