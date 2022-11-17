from functools import wraps

from flask import request

from utils.config import config
from utils.response import Response


def requires_api_key(func):
    @wraps(func)
    def decorated_function(*args, **kwargs):
        if x_api_key := request.headers.get("X-API-KEY", False):
            if config["X-API-KEY"] and x_api_key == config["X-API-KEY"]:
                return func(*args, **kwargs)

            return Response.error(message="X-API-KEY invalid.")

        return Response.error(message="X-API-KEY invalid.")

    return decorated_function
