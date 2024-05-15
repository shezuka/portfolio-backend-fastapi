from typing import Type

from fastapi import APIRouter
from sqlalchemy.orm import Session, joinedload

from portfolio_backend_fastapi.helpers.crud import CrudHelper, declare_crud_api
from portfolio_backend_fastapi.models import ModelSkillCategory, ModelBase
from portfolio_backend_fastapi.pydantic.requests.request_base import RequestBase
from portfolio_backend_fastapi.pydantic.requests.request_skill_category import RequestSkillCategory
from portfolio_backend_fastapi.pydantic.responses.response_base import ResponseBase
from portfolio_backend_fastapi.pydantic.responses.response_skill_category_detail import ResponseSkillCategoryDetail

skill_categories_router = APIRouter()


class SkillCategoriesCrudHelper(CrudHelper):
    RESOURCE_NAME: str = 'skill-categories'

    DB_MODEL: Type[ModelBase] = ModelSkillCategory
    CREATE_MODEL: Type[RequestBase] = RequestSkillCategory
    EDIT_MODEL: Type[RequestBase] = RequestSkillCategory
    RESPONSE_MODEL: Type[ResponseBase] = ResponseSkillCategoryDetail

    GET_LIST_API = True
    GET_API = True
    PUT_API = False
    POST_API = False
    DELETE_API = False

    REQUIRE_AUTH = False

    @classmethod
    def create_get_list_query(cls, db: Session):
        return db.query(cls.DB_MODEL).options(
            joinedload(ModelSkillCategory.skills)
        )


declare_crud_api(
    skill_categories_router,
    SkillCategoriesCrudHelper,
)
