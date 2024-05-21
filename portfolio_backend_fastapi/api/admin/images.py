import io
import math
from typing import Type

from PIL import Image
from fastapi import APIRouter, Depends, File, UploadFile, Body, Response
from sqlalchemy.orm import Session

from portfolio_backend_fastapi.dependencies.auth import assert_token
from portfolio_backend_fastapi.dependencies.db import get_db
from portfolio_backend_fastapi.helpers.crud import declare_crud_api, CrudHelper
from portfolio_backend_fastapi.models import ModelImage, ModelBase
from portfolio_backend_fastapi.pydantic.requests.request_base import RequestBase
from portfolio_backend_fastapi.pydantic.responses.response_base import ResponseBase
from portfolio_backend_fastapi.pydantic.responses.response_image import ResponseImage

admin_images_router = APIRouter()


class AdminSkillsCrudHelper(CrudHelper):
    RESOURCE_NAME: str = 'skills'

    DB_MODEL: Type[ModelBase] = ModelImage
    CREATE_MODEL: Type[RequestBase] = None
    EDIT_MODEL: Type[RequestBase] = None
    RESPONSE_MODEL: Type[ResponseBase] = ResponseImage

    GET_LIST_API = True
    GET_API = True
    PUT_API = False
    POST_API = False
    DELETE_API = True

    REQUIRE_AUTH = True

    @classmethod
    def get_build_response(cls, item: ModelImage):
        return Response(content=item.data, media_type=item.mime_type)


declare_crud_api(
    admin_images_router,
    AdminSkillsCrudHelper
)


@admin_images_router.post("", dependencies=[Depends(assert_token)])
async def upload_image(
        mime_type: str = Body(...),
        file: UploadFile = File(...),
        db: Session = Depends(get_db)
):
    MAX_IMAGE_SIZE = 320
    image_data = await file.read()

    image = Image.open(io.BytesIO(image_data))
    optimized_image_io = io.BytesIO()
    image = image.convert("RGB")
    if image.width > MAX_IMAGE_SIZE or image.height > MAX_IMAGE_SIZE:
        val = max(image.width, image.height)
        scale = MAX_IMAGE_SIZE / val
        image = image.resize((math.floor(image.width * scale), math.floor(image.height * scale)))
    image.save(optimized_image_io, format="JPEG", quality=80)
    optimized_image_io.seek(0)

    image = ModelImage()
    image.mime_type = 'image/jpeg'
    image.data = optimized_image_io.read()
    db.add(image)
    db.commit()
    db.refresh(image)
    return ResponseImage.from_orm(image)
