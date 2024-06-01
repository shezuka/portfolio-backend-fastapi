from sqlalchemy import String, Column, Text, Integer, ForeignKey
from sqlalchemy.orm import relationship

from .model_base import ModelBase


class ModelProject(ModelBase):
    __tablename__ = 'projects'

    title: str = Column(String, unique=True, nullable=False)
    description: str = Column(Text, nullable=False)
    image_id: int = Column(Integer, ForeignKey('images.id'), nullable=False)
    image = relationship('ModelImage')
    project_url: str = Column(String, nullable=True)
    frontend_github_url: str = Column(String, nullable=True)
    backend_github_url: str = Column(String, nullable=True)
