from sqlalchemy import Column, Integer, String, MetaData
from sqlalchemy.orm import declarative_base

Base = declarative_base()
metadata = MetaData()


class Pinyin(Base):
    __tablename__ = "pinyin"
    id = Column(Integer, primary_key=True)
    pinyin = Column(String)
