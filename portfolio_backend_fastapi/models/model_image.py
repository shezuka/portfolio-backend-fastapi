from sqlalchemy import Column, Integer, String, LargeBinary

from .model_base import ModelBase


class ModelImage(ModelBase):
    __tablename__ = 'images'

    entity_id = Column(Integer, nullable=False)
    entity_type = Column(String, nullable=False)
    mime_type = Column(String, nullable=False)
    title = Column(String, nullable=False)
    data = Column(LargeBinary, nullable=False)
