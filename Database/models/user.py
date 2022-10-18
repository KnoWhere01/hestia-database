from sqlalchemy import Column, Integer, String
from sqlalchemy.dialects.mysql import BIGINT

from utils.base import Base


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    username = Column(String(255), unique=True)
    password = Column(String(40))
    uploaded = Column(BIGINT(unsigned=True), default=0)
    downloaded = Column(BIGINT(unsigned=True), default=0)
