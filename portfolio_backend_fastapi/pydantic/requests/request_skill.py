from typing import Optional

from pydantic import Field

from portfolio_backend_fastapi.pydantic.requests.request_base import RequestBase


class RequestSkill(RequestBase):
    skill_category_id: int = Field(..., ge=0)
    title: str = Field(..., min_length=1)
    is_top: bool = Field(...)
