from sqlalchemy import String, Column, ForeignKey, Integer
from sqlalchemy.orm import relationship

from .model_base import ModelBase


class ModelSkill(ModelBase):
    __tablename__ = 'skills'

    category_id: int = Column(Integer, ForeignKey('skill_categories.id'))
    category = relationship("ModelSkillCategory")
    title: str = Column(String, unique=True)
