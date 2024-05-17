from typing import Optional

from portfolio_backend_fastapi.pydantic.responses.response_base import ResponseBase


class ResponseMessage(ResponseBase):
    name: str
    email: str
    message: str
