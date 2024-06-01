from sqlalchemy import String, Column, Integer
from sqlalchemy.orm import relationship

from .model_base import ModelBase


class ModelSkillCategory(ModelBase):
    __tablename__ = "skill_categories"

    order = Column(Integer)
    title = Column(String, unique=True)
    skills = relationship("ModelSkill", back_populates="skill_category")
