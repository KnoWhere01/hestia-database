import sqlalchemy
from sqlalchemy.orm import scoped_session, sessionmaker

from models.passkey import PassKey
from models.peer import Peer
from models.torrent import Torrent
from models.user import User
from models.password import Password
from utils.base import Base
from utils.config import Config
from utils.singleton import Singleton


class SQLAlchemy(metaclass=Singleton):
    def __init__(self) -> None:
        self.__config: dict = Config()

        self.db: sqlalchemy.engine.base.Engine = self.__connect()
        self.Session: sqlalchemy.orm.session.Session = self.__session()

        Base.metadata.create_all(self.db)

    def __connect(self) -> sqlalchemy.engine.base.Engine:
        database_config = self.__config["database"]

        database_ip = database_config["database_ip"]
        database_port = str(database_config["database_port"])
        database_name = database_config["database_name"]

        database_username = database_config["username"]
        database_password = database_config["password"]

        database_connector = database_config["database_connector"]
        return sqlalchemy.create_engine(
            f"{database_connector}://{database_username}:{database_password}@{database_ip}:{database_port}/{database_name}"
        )

    def __session(self):
        session = scoped_session(sessionmaker(self.db))
        return session()

    def add(self, *args) -> bool:
        for arg in args:
            self.Session.add(arg)

        return True

    def commit(self) -> bool:
        self.Session.commit()
        return True

    def close(self) -> bool:
        self.Session.close()
        return True

    def query(self, table):
        return self.Session.query(globals()[table])
