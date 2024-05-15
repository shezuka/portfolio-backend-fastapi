import datetime

from pydantic import BaseModel


class ResponseBase(BaseModel):
    __abstract__ = True

    id: int
    created_at: datetime.datetime
    updated_at: datetime.datetime

    class Config:
        from_attributes = True
