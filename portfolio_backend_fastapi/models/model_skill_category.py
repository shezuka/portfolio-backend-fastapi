from sqlalchemy import String, Column
from sqlalchemy.orm import relationship

from .model_base import ModelBase


class ModelSkillCategory(ModelBase):
    __tablename__ = "skill_categories"

    title = Column(String, unique=True)
    skills = relationship("ModelSkill", back_populates="category")
