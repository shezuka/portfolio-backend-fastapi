from sqlalchemy import String, Column

from .model_base import ModelBase


class ModelSkillCategory(ModelBase):
    __tablename__ = "skill_categories"

    title = Column(String, unique=True)
