import sqlalchemy
from models.base import Base
from models.passkey import PassKey
from models.peer import Peer
from models.torrent import Torrent
from models.user import User
from sqlalchemy.orm import scoped_session, sessionmaker


class SQLAlchemy:
    def __init__(self, config: dict) -> None:
        self.config: dict = config

        self.db: sqlalchemy.engine.base.Engine = self.connect()
        self.Session: sqlalchemy.orm.session.Session = self.session()

        Base.metadata.create_all(self.db)

    def connect(self) -> sqlalchemy.engine.base.Engine:
        database_config = self.config["database"]

        database_ip = database_config["database_ip"]
        database_port = str(database_config["database_port"])
        database_name = database_config["database_name"]

        database_username = database_config["username"]
        database_password = database_config["password"]

        database_connector = database_config["database_connector"]
        return sqlalchemy.create_engine(
            f"{database_connector}://{database_username}:{database_password}@{database_ip}:{database_port}/{database_name}"
        )

    def session(self):
        session = scoped_session(sessionmaker(self.db))
        return session()

    def add(self, object) -> bool:
        self.Session.add(object)
        return True

    def commit(self) -> bool:
        self.Session.commit()
        return True

    def close(self) -> bool:
        self.Session.close()
        return True

    def query(self, table):
        return self.Session.query(globals()[table])

    def test(self):
        print("test")