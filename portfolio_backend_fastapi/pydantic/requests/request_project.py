from typing import Optional

from pydantic import Field

from portfolio_backend_fastapi.pydantic.requests.request_base import RequestBase


class RequestProject(RequestBase):
    title: str = Field(..., min_length=1)
    description: str = Field(..., min_length=1)
    image_id: int = Field(..., gt=0)
    project_url: str = Field(None, min_length=1)
