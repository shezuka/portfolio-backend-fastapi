import datetime

from sqlalchemy import Column, Integer, String, Float, DateTime
from sqlalchemy.ext.declarative import declarative_base


class ModelBase(declarative_base()):
    __abstract__ = True

    id = Column(Integer, primary_key=True)
    created_at = Column(DateTime(True))
    updated_at = Column(DateTime(True))
