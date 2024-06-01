from portfolio_backend_fastapi.pydantic.responses.response_base import ResponseBase


class ResponseSkillCategory(ResponseBase):
    order: int
    title: str
