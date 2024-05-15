from portfolio_backend_fastapi.pydantic.requests.request_base import RequestBase


class RequestLogin(RequestBase):
    username: str
    password: str
