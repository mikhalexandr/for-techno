from pydantic import BaseModel


class CustomExceptionResponse(BaseModel):
    status: str
    message: str
