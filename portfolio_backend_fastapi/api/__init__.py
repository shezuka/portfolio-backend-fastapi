from fastapi import APIRouter

from portfolio_backend_fastapi.api.admin import admin_router
from portfolio_backend_fastapi.api.auth import auth_router
from portfolio_backend_fastapi.api.images import images_router
from portfolio_backend_fastapi.api.messages import messages_router
from portfolio_backend_fastapi.api.projects import projects_router
from portfolio_backend_fastapi.api.skill_categories import skill_categories_router
from portfolio_backend_fastapi.api.skills import skills_router

api_router = APIRouter()
api_router.include_router(auth_router, prefix="/auth")
api_router.include_router(admin_router, prefix="/admin")
api_router.include_router(images_router, prefix="/images")
api_router.include_router(projects_router, prefix="/projects")
api_router.include_router(skill_categories_router, prefix="/skill-categories")
api_router.include_router(skills_router, prefix="/skills")
api_router.include_router(messages_router, prefix="/messages")
