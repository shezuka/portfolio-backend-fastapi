from fastapi import APIRouter

from portfolio_backend_fastapi.api.admin.images import admin_images_router
from portfolio_backend_fastapi.api.admin.messages import admin_messages_router
from portfolio_backend_fastapi.api.admin.projects import admin_projects_router
from portfolio_backend_fastapi.api.admin.skill_categories import admin_skill_categories_router
from portfolio_backend_fastapi.api.admin.skills import admin_skills_router

admin_router = APIRouter()
admin_router.include_router(admin_images_router, prefix="/images")
admin_router.include_router(admin_skill_categories_router, prefix="/skill-categories")
admin_router.include_router(admin_skills_router, prefix="/skills")
admin_router.include_router(admin_projects_router, prefix="/projects")
admin_router.include_router(admin_messages_router, prefix="/messages")
