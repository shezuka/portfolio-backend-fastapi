from portfolio_backend_fastapi.pydantic.responses.response_base import ResponseBase


class ResponseToken(ResponseBase):
    access_token: str
