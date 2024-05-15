from portfolio_backend_fastapi.pydantic.responses.response_base import ResponseBase


class ResponseUser(ResponseBase):
    id: int
    username: str
