import utils.yaml as yaml
from utils.singleton import Singleton


class Config(metaclass=Singleton):
    def __new__(cls) -> dict:
        return yaml.read(".env")


config = Config()
