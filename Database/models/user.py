from sqlalchemy import Column, Integer, String
from sqlalchemy.dialects.mysql import BIGINT

from utils.base import Base


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    username = Column(String(255), unique=True)
    password = Column(String(60))
    uploaded = Column(BIGINT(unsigned=True), default=0)
    downloaded = Column(BIGINT(unsigned=True), default=0)

    def __repr__(self):
        return (
            "<User(username='%s', password='%s', uploaded='%s', downloaded='%s')>"
            % (self.username, self.password, self.uploaded, self.downloaded)
        )
