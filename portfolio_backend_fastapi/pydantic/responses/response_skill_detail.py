from portfolio_backend_fastapi.pydantic.responses.response_skill import ResponseSkill
from portfolio_backend_fastapi.pydantic.responses.response_skill_category import ResponseSkillCategory


class ResponseSkillDetail(ResponseSkill):
    category: ResponseSkillCategory
