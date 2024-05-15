from typing import Optional

from portfolio_backend_fastapi.pydantic.responses.response_base import ResponseBase


class ResponseProject(ResponseBase):
    title: str
    description: str
    image_id: int
    project_url: Optional[str]
