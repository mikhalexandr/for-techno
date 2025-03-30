from pydantic import BaseModel


class HealthcheckRootRs(BaseModel):
    status: str
    current_time: str


class HealthcheckPingRs(BaseModel):
    status: str
    response_time: float
