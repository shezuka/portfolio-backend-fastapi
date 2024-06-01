from pydantic import BaseModel


class RequestBase(BaseModel):
    __abstract__ = True
