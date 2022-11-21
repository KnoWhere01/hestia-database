from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.dialects.mysql import BIGINT, TINYINT
from sqlalchemy.orm import relationship

from models.torrent import Torrent
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
    left = Column(BIGINT(unsigned=True), default=0)
    event = Column(TINYINT, default=0)
    tracker_id = Column(String(40))
    compact = Column(Boolean, default=False)
    key = Column(String(40))
    corrupt = Column(Boolean, default=False)
    no_peer_id = Column(Boolean, default=False)
    user_agent = Column(String(1000))

    relationship(Torrent, backref="peers")

    def __repr__(self):
        return "<Peer(torrent='%s', peer_id='%s', ip='%s', port='%s', uploaded='%s', downloaded='%s', left='%s', event='%s', tracker_id='%s', compact='%s', key='%s', corrupt='%s', no_peer_id='%s', user_agent='%s')>" % (
            self.torrent,
            self.peer_id,
            self.ip,
            self.port,
            self.uploaded,
            self.downloaded,
            self.left,
            self.event,
            self.tracker_id,
            self.compact,
            self.key,
            self.corrupt,
            self.no_peer_id,
            self.user_agent,
        )
