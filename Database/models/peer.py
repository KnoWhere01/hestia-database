from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.dialects.mysql import BIGINT, TINYINT
from sqlalchemy.orm import relationship

from utils.models import Torrent
from utils.base import Base


class Peer(Base):
    __tablename__ = "peers"
    id = Column(Integer, primary_key=True)
    torrent = Column(Integer, ForeignKey("torrents.id"))
    peer_id = Column(String(40))
    ip = Column(String(45))
    port = Column(Integer)
    uploaded = Column(BIGINT(unsigned=True), default=0)
    downloaded = Column(BIGINT(unsigned=True), default=0)
    uploaded_total = Column(BIGINT(unsigned=True), default=0)
    downloaded_total = Column(BIGINT(unsigned=True), default=0)
    seeding = Column(Boolean, default=False)
    user_agent = Column(String(1000))

    relationship(Torrent, backref="peers")

    def __repr__(self):
        return "<Peer(torrent='%s', peer_id='%s', ip='%s', port='%s', uploaded='%s', downloaded='%s', uploaded_total='%s', downloaded_total='%s', seeding='%s', user_agent='%s')>" % (
            self.torrent,
            self.peer_id,
            self.ip,
            self.port,
            self.uploaded,
            self.downloaded,
            self.uploaded_total,
            self.downloaded_total,
            self.seeding,
            self.user_agent,
        )
