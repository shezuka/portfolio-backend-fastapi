from typing import Type

from fastapi import APIRouter
from sqlalchemy.orm import Session

from portfolio_backend_fastapi.helpers.crud import CrudHelper, declare_crud_api
from portfolio_backend_fastapi.models import ModelSkillCategory, ModelBase
from portfolio_backend_fastapi.pydantic.requests.request_base import RequestBase
from portfolio_backend_fastapi.pydantic.requests.request_skill_category import RequestSkillCategory
from portfolio_backend_fastapi.pydantic.responses.response_base import ResponseBase
from portfolio_backend_fastapi.pydantic.responses.response_skill_category import ResponseSkillCategory

admin_skill_categories_router = APIRouter()


class AdminSkillCategoriesCrudHelper(CrudHelper):
    RESOURCE_NAME: str = 'skill-categories'

    DB_MODEL: Type[ModelBase] = ModelSkillCategory
    CREATE_MODEL: Type[RequestBase] = RequestSkillCategory
    EDIT_MODEL: Type[RequestBase] = RequestSkillCategory
    RESPONSE_MODEL: Type[ResponseBase] = ResponseSkillCategory

    GET_LIST_API = True
    GET_API = True
    PUT_API = True
    POST_API = True
    DELETE_API = True

    REQUIRE_AUTH = True

    @classmethod
    def insert_on_before_execute_query(cls, db: Session, request: RequestBase):
        if request.order is None or request.order == -1:
            request.order = db.query(ModelSkillCategory).count()
        else:
            (
                db.query(ModelSkillCategory)
                .filter(ModelSkillCategory.order >= request.order)
                .update({ModelSkillCategory.order: ModelSkillCategory.order + 1})
            )

    @classmethod
    def update_on_before_execute_query(cls, db: Session, item: ModelSkillCategory, request: RequestBase):
        (
            db.query(ModelSkillCategory)
            .filter(ModelSkillCategory.order > item.order)
            .filter(ModelSkillCategory.id != item.id)
            .update({ModelSkillCategory.order: ModelSkillCategory.order - 1})
        )
        (
            db.query(ModelSkillCategory)
            .filter(ModelSkillCategory.id != item.id)
            .filter(ModelSkillCategory.order >= request.order)
            .update({ModelSkillCategory.order: ModelSkillCategory.order + 1})
        )

    @classmethod
    def delete_on_deleted(cls, db: Session, item: ModelBase):
        (
            db.query(ModelSkillCategory)
            .filter(ModelSkillCategory.order > item.order)
            .update({ModelSkillCategory.order: ModelSkillCategory.order - 1})
        )


declare_crud_api(
    admin_skill_categories_router,
    AdminSkillCategoriesCrudHelper,
)
