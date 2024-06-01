from sqlalchemy import String, Column

from .model_base import ModelBase


class ModelUser(ModelBase):
    __tablename__ = 'users'

    username = Column(String(50), unique=True, nullable=False)
    password = Column(String(255), nullable=False)
