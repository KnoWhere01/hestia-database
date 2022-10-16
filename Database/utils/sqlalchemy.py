import yaml
from flask_sqlalchemy import SQLAlchemy as DataBase

import utils.yaml as yaml


class SQLAlchemy:
    def __init__(self, flask):
        self.flask = flask
        self.database = DataBase()

    def config(self):
        database_config = yaml.read(".env")["database"]

        database_connector = database_config["database_connector"]

        database_ip = database_config["database_ip"]
        database_port = str(database_config["database_port"])
        database_name = database_config["database_name"]

        database_username = database_config["username"]
        database_password = database_config["password"]

        self.flask.config["SQLALCHEMY_DATABASE_URI"] = (
            database_connector
            + "://"
            + database_username
            + ":"
            + database_password
            + "@"
            + database_ip
            + ":"
            + database_port
            + "/"
            + database_name
        )

        self.flask.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

        self.database.init_app(self.flask)

        return True
