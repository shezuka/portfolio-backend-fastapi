from portfolio_backend_fastapi.pydantic.responses.response_base import ResponseBase


class ResponseSkill(ResponseBase):
    skill_category_id: int
    title: str
    is_top: bool
