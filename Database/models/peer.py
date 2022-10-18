from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.dialects.mysql import BIGINT, TINYINT
from sqlalchemy.orm import relationship

from models.torrent import Torrent
from utils.base import Base


class Peer(Base):
    __tablename__ = "peers"
    id = Column(Integer, primary_key=True)
    torrent_id = Column(Integer, ForeignKey("torrents.id"))
    peer_id = Column(String(40))
    ip = Column(String(45))
    port = Column(Integer)
    uploaded = Column(BIGINT(unsigned=True), default=0)
    downloaded = Column(BIGINT(unsigned=True), default=0)
    left = Column(BIGINT(unsigned=True), default=0)
    event = Column(TINYINT, default=0)
    tracker_id = Column(String(40))
    compact = Column(Boolean, default=False)
    key = Column(String(40))
    corrupt = Column(Boolean, default=False)
    no_peer_id = Column(Boolean, default=False)
    user_agent = Column(String(1000))

    torrent = relationship(Torrent, backref="peers")
