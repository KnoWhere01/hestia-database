from sqlalchemy import Column, DateTime, ForeignKey, Integer, String
from sqlalchemy.dialects.mysql import BIGINT, TINYINT
from sqlalchemy.orm import relationship

from models.user import User
from utils.base import Base


class Torrent(Base):
    __tablename__ = "torrents"
    id = Column(Integer, primary_key=True)
    uploader = Column(Integer, ForeignKey("users.id"))
    info_hash = Column(String(40))
    name = Column(String(255))
    desc = Column(String(1000))
    torrent_file = Column(String(255))
    torrent_version = Column(TINYINT, default=1)
    uploaded_time = Column(DateTime)
    download_count = Column(BIGINT(unsigned=True), default=0)
    seeders = Column(BIGINT(unsigned=True), default=0)
    leechers = Column(BIGINT(unsigned=True), default=0)
    last_checked = Column(DateTime)

    relationship(User, backref="torrents")
