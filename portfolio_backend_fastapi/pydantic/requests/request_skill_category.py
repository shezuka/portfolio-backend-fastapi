from typing import Optional

from pydantic import Field

from portfolio_backend_fastapi.pydantic.requests.request_base import RequestBase


class RequestSkillCategory(RequestBase):
    title: str = Field(..., min_length=1)
    order: Optional[int] = Field(-1)
