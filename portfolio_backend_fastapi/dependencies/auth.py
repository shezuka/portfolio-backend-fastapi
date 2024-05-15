from typing import Annotated

import jwt
from fastapi import Header, Depends, HTTPException

from portfolio_backend_fastapi.config import APP_SECRET


async def get_token(authorization: Annotated[str, Header()]):
    token = authorization.split(" ")[-1]
    if not token:
        return None

    try:
        decoded = jwt.decode(token, APP_SECRET, algorithms=["HS256"])
        return decoded
    except jwt.DecodeError as e:
        return None


async def assert_token(token: str = Depends(get_token)) -> str:
    if token is None:
        raise HTTPException(status_code=401, detail="Unauthorized")
    return token
