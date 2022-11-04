from html import escape

from flask import request

from utils.blueprint import Blueprint
from utils.response import Response
from utils.sqlalchemy import SQLAlchemy

from utils.security import requires_api_key

blueprint = Blueprint("passkey_update")

database: SQLAlchemy = SQLAlchemy()


@blueprint.route("/passkey/<passKey>", methods=["PATCH", "PUT"])
@requires_api_key
def passkey_update(passKey):
    """Passkey UPDATE"""
    if passKey := escape(passKey):
        if passKey := database.query("PassKey").filter_by(passkey=passKey):
            torrent = request.json.get("torrent", False)
            user = request.json.get("user", 0)

            if torrent:
                passKey.update({"torrent": torrent})

            if user:
                passKey.update({"user": user})

            if database.commit():
                passKey = passKey.limit(1).first()

                return Response.success(
                    message={
                        "passkey": passKey.passkey,
                        "torrent": passKey.torrent,
                        "user": passKey.user,
                    }
                )

        return Response.error(message="PassKey unavailable.")

    return Response.error(message="Error during passkey update.")
