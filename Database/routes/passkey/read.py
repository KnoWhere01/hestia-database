from flask import request

from utils.blueprint import Blueprint
from utils.response import Response
from utils.sqlalchemy import SQLAlchemy

from html import escape

blueprint = Blueprint("passkey_read")

database: SQLAlchemy = SQLAlchemy()


@blueprint.route("/passkey/<passKey>", methods=["GET"])
def passkey_read(passKey):
    """Passkey READ"""

    if passKey := escape(passKey):
        if passKey := database.query("PassKey").filter_by(passkey=passKey).limit(1).first():
            return Response.success(
                message={
                    "passkey": passKey.passkey,
                    "torrent": passKey.torrent,
                    "user": passKey.user,
                }
            )

        return Response.error(message="PassKey unavailable.")

    return Response.error(message="PassKey unavailable.")
