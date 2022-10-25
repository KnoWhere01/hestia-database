from sqlalchemy import Column, ForeignKey, Integer, String

from utils.base import Base


class PassKey(Base):
    __tablename__ = "passkeys"
    id = Column(Integer, primary_key=True)
    passkey = Column(String(36), unique=True)
    torrent = Column(Integer, ForeignKey("torrents.id"))
    user = Column(Integer, ForeignKey("users.id"))

    def __repr__(self):
        return (
            "<PassKey(passkey='%s', torrent='%s', user='%s')>"
            % (
                self.passkey,
                self.torrent,
                self.user,
            )
        )
