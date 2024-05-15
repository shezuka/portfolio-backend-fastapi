from typing import Type

from fastapi import APIRouter

from portfolio_backend_fastapi.helpers.crud import CrudHelper, declare_crud_api
from portfolio_backend_fastapi.models import ModelProject, ModelBase
from portfolio_backend_fastapi.pydantic.requests.request_base import RequestBase
from portfolio_backend_fastapi.pydantic.requests.request_project import RequestProject
from portfolio_backend_fastapi.pydantic.responses.response_base import ResponseBase
from portfolio_backend_fastapi.pydantic.responses.response_project import ResponseProject

projects_router = APIRouter()


class ProjectsCrudHelper(CrudHelper):
    RESOURCE_NAME: str = 'projects'

    DB_MODEL: Type[ModelBase] = ModelProject
    CREATE_MODEL: Type[RequestBase] = RequestProject
    EDIT_MODEL: Type[RequestBase] = RequestProject
    RESPONSE_MODEL: Type[ResponseBase] = ResponseProject

    GET_LIST_API = True
    GET_API = True
    PUT_API = False
    POST_API = False
    DELETE_API = False

    REQUIRE_AUTH = False


declare_crud_api(
    projects_router,
    ProjectsCrudHelper,
)
