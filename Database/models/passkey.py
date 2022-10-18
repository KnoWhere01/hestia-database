from sqlalchemy import Column, ForeignKey, Integer, String

from models.base import Base


class PassKey(Base):
    __tablename__ = "passkeys"
    id = Column(Integer, primary_key=True)
    passkey = Column(String(36))
    torrent = Column(Integer, ForeignKey("torrents.id"))
    user = Column(Integer, ForeignKey("users.id"))
