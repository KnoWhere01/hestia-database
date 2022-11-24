from sqlalchemy import Column, Integer, String
from sqlalchemy.dialects.mysql import BIGINT
from sqlalchemy_serializer import SerializerMixin

from utils.base import Base


class User(Base, SerializerMixin):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    username = Column(String(255), unique=True, nullable=False)
    api_key = Column(String(36), unique=True, nullable=False)
    uploaded = Column(BIGINT(unsigned=True), default=0)
    downloaded = Column(BIGINT(unsigned=True), default=0)

    def __repr__(self):
        return "<User(username='%s', api_key='%s', uploaded='%s', downloaded='%s')>" % (
            self.username,
            self.api_key,
            self.uploaded,
            self.downloaded,
        )
