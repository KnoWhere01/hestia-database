from flask import request

from utils.blueprint import Blueprint
from utils.response import Response
from utils.sqlalchemy import SQLAlchemy

from html import escape

blueprint = Blueprint("user_read")

database: SQLAlchemy = SQLAlchemy()


@blueprint.route("/user/<user>", methods=["GET"])
def user_read(user):
    """User READ"""

    if username := escape(user):
        if user := database.query("User").filter_by(username=username).limit(1).first():
            return Response.success(
                message={
                    "username": user.username,
                    "uploaded": user.uploaded,
                    "downloaded": user.downloaded,
                }
            )

        return Response.error(message="Username unavailable.")

    return Response.error(message="Username unavailable.")
