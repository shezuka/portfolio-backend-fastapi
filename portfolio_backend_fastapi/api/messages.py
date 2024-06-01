from typing import Type

from fastapi import APIRouter

from portfolio_backend_fastapi.helpers.crud import CrudHelper, declare_crud_api
from portfolio_backend_fastapi.models import ModelBase, ModelMessage
from portfolio_backend_fastapi.pydantic.requests.request_base import RequestBase
from portfolio_backend_fastapi.pydantic.requests.request_message import RequestMessage
from portfolio_backend_fastapi.pydantic.responses.response_base import ResponseBase
from portfolio_backend_fastapi.pydantic.responses.response_message import ResponseMessage

messages_router = APIRouter()


class MessageCrudHelper(CrudHelper):
    RESOURCE_NAME: str = 'messages'

    DB_MODEL: Type[ModelBase] = ModelMessage
    CREATE_MODEL: Type[RequestBase] = RequestMessage
    EDIT_MODEL: Type[RequestBase] = RequestMessage
    RESPONSE_MODEL: Type[ResponseBase] = ResponseMessage

    GET_LIST_API = False
    GET_API = False
    PUT_API = False
    POST_API = True
    DELETE_API = False

    REQUIRE_AUTH = False

    POST_CAPTCHA_PROTECTED = True
    POST_CAPTCHA_ACTION = 'send_message'


declare_crud_api(
    messages_router,
    MessageCrudHelper,
)
