from utils.singleton import Singleton

class Response(object, metaclass=Singleton):
    @staticmethod
    def success(message: str, code: int = 200):
        return {
        "success": True,
        "message": message,
    }, code
    
    @staticmethod
    def error(message: str, code: int = 403):
        return {
        "success": False,
        "message": message,
    }, code