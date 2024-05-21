from typing import Optional

from pydantic import Field

from portfolio_backend_fastapi.pydantic.requests.request_base import RequestBase


class RequestProject(RequestBase):
    title: str = Field(..., min_length=1)
    description: str = Field(..., min_length=1)
    image_id: int = Field(..., gt=0)
    project_url: Optional[str] = Field(..., min_length=1)
    frontend_github_url: Optional[str] = Field(..., min_length=1)
    backend_github_url: Optional[str] = Field(..., min_length=1)
