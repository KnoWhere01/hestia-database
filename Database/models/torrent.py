from sqlalchemy import Column, DateTime, ForeignKey, Integer, String
from sqlalchemy.dialects.mysql import BIGINT, TINYINT
from sqlalchemy.orm import relationship

from models.user import User
from utils.base import Base

from sqlalchemy_serializer import SerializerMixin

class Torrent(Base, SerializerMixin):
    __tablename__ = "torrents"
    id = Column(Integer, primary_key=True)
    uploader = Column(Integer, ForeignKey("users.id"))
    info_hash = Column(String(40))
    name = Column(String(255))
    desc = Column(String(1000))
    torrent_file = Column(String(255))
    version = Column(TINYINT, default=1)
    uploaded_time = Column(DateTime)
    download_count = Column(BIGINT(unsigned=True), default=0)
    seeders = Column(BIGINT(unsigned=True), default=0)
    leechers = Column(BIGINT(unsigned=True), default=0)
    last_checked = Column(DateTime)

    relationship(User, backref="torrents")

    def __repr__(self):
        return (
            "<Torrent(uploader='%s', info_hash='%s', name='%s', desc='%s', torrent_file='%s', version='%s', uploaded_time='%s', download_count='%s', seeders='%s', leechers='%s', last_checked='%s')>"
            % (
                self.uploader,
                self.info_hash,
                self.name,
                self.desc,
                self.torrent_file,
                self.version,
                self.uploaded_time,
                self.download_count,
                self.seeders,
                self.leechers,
                self.last_checked,
            )
        )
