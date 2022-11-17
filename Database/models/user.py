from sqlalchemy import Column, Integer, String
from sqlalchemy.dialects.mysql import BIGINT

from utils.base import Base


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    username = Column(String(255), unique=True)
    uploaded = Column(BIGINT(unsigned=True), default=0)
    downloaded = Column(BIGINT(unsigned=True), default=0)

    def __repr__(self):
        return (
            "<User(username='%s', uploaded='%s', downloaded='%s')>"
            % (self.username, self.uploaded, self.downloaded)
        )
