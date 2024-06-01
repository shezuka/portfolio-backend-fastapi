from fastapi import FastAPI

from portfolio_backend_fastapi.api import api_router

app = FastAPI()
app.include_router(api_router, prefix="/api")
