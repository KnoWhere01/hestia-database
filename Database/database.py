from flask import Flask
from gevent.pywsgi import WSGIServer
from routes.routes import set_routes


class Database:
    def __init__(self) -> None:
        self.flask: Flask = Flask(__name__)

    def start(self) -> None:
        if set_routes(self.flask):
            WSGIServer(("0.0.0.0", 5000), self.flask).serve_forever()


if __name__ == "__main__":
    Database().start()
