from sqlalchemy import String, Column, ForeignKey, Integer, Boolean
from sqlalchemy.orm import relationship

from .model_base import ModelBase


class ModelSkill(ModelBase):
    __tablename__ = 'skills'

    skill_category_id: int = Column(Integer, ForeignKey('skill_categories.id'))
    skill_category = relationship("ModelSkillCategory", back_populates="skills")
    title: str = Column(String, unique=True)
    is_top: bool = Column(Boolean, nullable=False, default=False)
