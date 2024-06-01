from sqlalchemy import Column, String, Text

from .model_base import ModelBase


class ModelMessage(ModelBase):
    __tablename__ = 'messages'

    name = Column(String(128), nullable=False)
    email = Column(String(128), nullable=False)
    message = Column(Text(), nullable=False)
