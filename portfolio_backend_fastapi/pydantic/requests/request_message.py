from typing import Optional

from pydantic import Field

from portfolio_backend_fastapi.pydantic.requests.request_base import RequestBase


class RequestMessage(RequestBase):
    name: str = Field(..., min_length=1)
    email: str = Field(..., min_length=1)
    message: str = Field(..., min_length=1)
