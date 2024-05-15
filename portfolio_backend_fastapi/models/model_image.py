from sqlalchemy import Column, Integer, String, LargeBinary

from .model_base import ModelBase


class ModelImage(ModelBase):
    __tablename__ = 'images'

    mime_type = Column(String, nullable=False)
    data = Column(LargeBinary, nullable=False)
