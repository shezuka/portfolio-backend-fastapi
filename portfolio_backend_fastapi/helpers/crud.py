import ast
from typing import Type, Optional

import sqlalchemy
from fastapi import APIRouter, Depends, Response, Query
from sqlalchemy.orm import Session

from portfolio_backend_fastapi.dependencies.auth import assert_token
from portfolio_backend_fastapi.dependencies.db import get_db
from portfolio_backend_fastapi.models import ModelBase
from portfolio_backend_fastapi.pydantic.requests.request_base import RequestBase
from portfolio_backend_fastapi.pydantic.responses.response_base import ResponseBase


class CrudHelper:
    RESOURCE_NAME: str

    DB_MODEL: Type[ModelBase]
    CREATE_MODEL: Type[RequestBase]
    EDIT_MODEL: Type[RequestBase]
    RESPONSE_MODEL: Type[ResponseBase]

    GET_LIST_API = True
    GET_API = True
    PUT_API = True
    POST_API = True
    DELETE_API = True

    REQUIRE_AUTH = False

    @classmethod
    def create_get_list_query(cls, db: Session):
        return db.query(cls.DB_MODEL)

    @classmethod
    def get_list_query_filters(cls, query: sqlalchemy.orm.Query):
        return query

    @classmethod
    def get_build_response(cls, item: ModelBase):
        return cls.RESPONSE_MODEL.from_orm(item)

    @classmethod
    def insert_create_model(cls, db: Session, request: RequestBase):
        return cls.DB_MODEL(**request.dict())

    @classmethod
    def insert_on_before_execute_query(cls, db: Session, request: RequestBase):
        pass

    @classmethod
    def update_get_model(cls, db: Session, id: int):
        return db.query(cls.DB_MODEL).filter(cls.DB_MODEL.id == id).first()

    @classmethod
    def update_on_before_execute_query(cls, db: Session, item: ModelBase, request: RequestBase):
        pass

    @classmethod
    def update_on_after_execute_query(cls, db: Session, item: ModelBase, request: RequestBase):
        pass

    @classmethod
    def delete_on_deleted(cls, db: Session, item: ModelBase):
        pass


def declare_crud_api(
        router: APIRouter,
        helper: Type[CrudHelper]
):
    dependencies = []

    if helper.REQUIRE_AUTH:
        dependencies.append(Depends(assert_token))

    if helper.GET_LIST_API:
        @router.get("", dependencies=dependencies)
        async def get_range(
                response: Response,
                filter: Optional[str] = Query("{}"),
                range: Optional[str] = Query("[0,100]"),
                sort: Optional[str] = Query("['id', 'DESC']"),
                db: Session = Depends(get_db)
        ):
            try:
                filter = ast.literal_eval(filter)
            except (SyntaxError, ValueError, TypeError):
                filter = {}

            try:
                range = ast.literal_eval(range)
            except (SyntaxError, ValueError, TypeError):
                range = [0, 100]

            try:
                sort = ast.literal_eval(sort)
            except (SyntaxError, ValueError, TypeError):
                sort = ['id', 'DESC']

            sort_field = sort[0]
            sort_direction = sort[1]
            sorting = None
            if hasattr(helper.DB_MODEL, sort_field):
                attr = getattr(helper.DB_MODEL, sort_field)
                if sort_direction == 'ASC':
                    sorting = attr.asc()
                elif sort_direction == 'DESC':
                    sorting = attr.desc()

            query = helper.create_get_list_query(db)
            query = helper.get_list_query_filters(query)

            for key, value in filter.items():
                if not hasattr(helper.DB_MODEL, key):
                    continue

                if isinstance(value, list):
                    query = query.filter(getattr(helper.DB_MODEL, key).in_(value))
                else:
                    query = query.filter(getattr(helper.DB_MODEL, key) == value)

            total = query.count()

            if sorting is not None:
                query = query.order_by(sorting)

            items = query.offset(range[0]).limit(range[1] - range[0] + 1).all()
            response.headers['Content-Range'] = f'{helper.RESOURCE_NAME} {range[0]}-{range[0] + len(items)}/{total}'
            return [helper.RESPONSE_MODEL.from_orm(item) for item in items]

    if helper.GET_API:
        @router.get("/{id}", response_model=helper.RESPONSE_MODEL, dependencies=dependencies)
        async def get(
                id: int,
                db: Session = Depends(get_db)
        ):
            item = (
                db.query(helper.DB_MODEL)
                .filter(helper.DB_MODEL.id == id)
                .first()
            )
            if item is None:
                return Response(status_code=404)
            return helper.get_build_response(item)

    if helper.POST_API:
        @router.post("", response_model=helper.RESPONSE_MODEL, dependencies=dependencies)
        async def create(
                request: helper.CREATE_MODEL,
                db: Session = Depends(get_db)
        ):
            helper.insert_on_before_execute_query(db, request)
            item = helper.insert_create_model(db, request)
            db.add(item)
            db.commit()
            db.refresh(item)
            return helper.RESPONSE_MODEL.from_orm(item)

    if helper.PUT_API:
        @router.put("/{id}", response_model=helper.RESPONSE_MODEL, dependencies=dependencies)
        async def update(
                id: int,
                request: helper.EDIT_MODEL,
                db: Session = Depends(get_db)
        ):
            item = helper.update_get_model(db, id)
            if item is None:
                return Response(status_code=404)
            helper.update_on_before_execute_query(db, item, request)
            for key, value in request.dict().items():
                if hasattr(item, key):
                    setattr(item, key, value)
            helper.update_on_after_execute_query(db, item, request)
            db.add(item)
            db.commit()
            db.refresh(item)
            return helper.RESPONSE_MODEL.from_orm(item)

    if helper.DELETE_API:
        @router.delete("/{id}", dependencies=dependencies)
        async def delete(
                id: int,
                db: Session = Depends(get_db)
        ):
            item = (
                db.query(helper.DB_MODEL)
                .filter(helper.DB_MODEL.id == id)
                .first()
            )
            if item is None:
                return Response(status_code=404)
            db.delete(item)
            helper.delete_on_deleted(db, item)
            db.commit()
            return {}
