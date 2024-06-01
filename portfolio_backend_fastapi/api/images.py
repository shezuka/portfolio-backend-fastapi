from typing import Type

from fastapi import APIRouter, Response

from portfolio_backend_fastapi.helpers.crud import declare_crud_api
from portfolio_backend_fastapi.models import ModelImage, ModelBase
from portfolio_backend_fastapi.pydantic.requests.request_base import RequestBase
from portfolio_backend_fastapi.pydantic.responses.response_base import ResponseBase
from portfolio_backend_fastapi.pydantic.responses.response_image import ResponseImage

images_router = APIRouter()


class ImagesCrudHelper:
    RESOURCE_NAME: str = 'images'

    DB_MODEL: Type[ModelBase] = ModelImage
    CREATE_MODEL: Type[RequestBase] = None
    EDIT_MODEL: Type[RequestBase] = None
    RESPONSE_MODEL: Type[ResponseBase] = ResponseImage

    GET_LIST_API = True
    GET_API = True
    PUT_API = False
    POST_API = False
    DELETE_API = False

    REQUIRE_AUTH = False

    @classmethod
    def get_build_response(cls, item: ModelImage):
        return Response(content=item.data, media_type=item.mime_type)


declare_crud_api(
    images_router,
    ImagesCrudHelper,
)
