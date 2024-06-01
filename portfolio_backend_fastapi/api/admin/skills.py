from typing import Type

from fastapi import APIRouter

from portfolio_backend_fastapi.helpers.crud import CrudHelper, declare_crud_api
from portfolio_backend_fastapi.models import ModelBase, ModelSkill
from portfolio_backend_fastapi.pydantic.requests.request_base import RequestBase
from portfolio_backend_fastapi.pydantic.requests.request_skill import RequestSkill
from portfolio_backend_fastapi.pydantic.responses.response_base import ResponseBase
from portfolio_backend_fastapi.pydantic.responses.response_skill import ResponseSkill

admin_skills_router = APIRouter()


class AdminSkillsCrudHelper(CrudHelper):
    RESOURCE_NAME: str = 'skills'

    DB_MODEL: Type[ModelBase] = ModelSkill
    CREATE_MODEL: Type[RequestBase] = RequestSkill
    EDIT_MODEL: Type[RequestBase] = RequestSkill
    RESPONSE_MODEL: Type[ResponseBase] = ResponseSkill

    GET_LIST_API = True
    GET_API = True
    PUT_API = True
    POST_API = True
    DELETE_API = True

    REQUIRE_AUTH = True


declare_crud_api(
    admin_skills_router,
    AdminSkillsCrudHelper,
)
