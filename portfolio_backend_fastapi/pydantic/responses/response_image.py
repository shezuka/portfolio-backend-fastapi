from portfolio_backend_fastapi.pydantic.responses.response_base import ResponseBase


class ResponseImage(ResponseBase):
    mime_type: str
