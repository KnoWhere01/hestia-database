from typing import Union

from utils.singleton import Singleton


class Response(object, metaclass=Singleton):
    @staticmethod
    def success(message: Union[str, dict], code: int = 200):
        return {
            "success": True,
            "message": message,
        }, code

    @staticmethod
    def error(message: Union[str, dict], code: int = 403):
        return {
            "success": False,
            "message": message,
        }, code
