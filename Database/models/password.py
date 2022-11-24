from sqlalchemy import Column, Integer, String
from sqlalchemy.dialects.mysql import BIGINT
from sqlalchemy_serializer import SerializerMixin

from utils.base import Base


class Password(Base, SerializerMixin):
    __tablename__ = "passwords"
    id = Column(Integer, primary_key=True)
    user = Column(BIGINT(unsigned=True), nullable=False)
    password = Column(String(60), nullable=False)

    def __repr__(self):
        return "<Password(user='%s', password='%s')>" % (
            self.user,
            self.password,
        )
