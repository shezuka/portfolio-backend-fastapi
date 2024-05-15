import datetime

import jwt
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from portfolio_backend_fastapi.config import APP_SECRET
from portfolio_backend_fastapi.dependencies.db import get_db
from portfolio_backend_fastapi.lib.password import verify_password, hash_password
from portfolio_backend_fastapi.models import ModelUser
from portfolio_backend_fastapi.pydantic.requests.request_login import RequestLogin
from portfolio_backend_fastapi.pydantic.responses.response_token import ResponseToken

auth_router = APIRouter()


@auth_router.post("/login")
async def login(request_login: RequestLogin, db: Session = Depends(get_db)):
    if db.query(ModelUser).count() == 0:
        user = ModelUser()
        user.username = request_login.username
        user.password = hash_password(request_login.password)
        db.add(user)
        db.commit()
        db.refresh(user)
    else:
        user = db.query(ModelUser).filter(ModelUser.username == request_login.username).first()
        if not user:
            raise HTTPException(status_code=401, detail="Unauthorized")

        if not verify_password(request_login.password, user.password):
            raise HTTPException(status_code=401, detail="Unauthorized")

    payload = {"id": user.id, "exp": datetime.datetime.now() + datetime.timedelta(days=1)}
    token = jwt.encode(payload, APP_SECRET, algorithm="HS256")
    return {"access_token": token}
