import uuid

from flask import request
from models.passkey import PassKey
from utils.blueprint import Blueprint
from utils.sqlalchemy import SQLAlchemy

blueprint = Blueprint("passkey_create")

database: SQLAlchemy = SQLAlchemy()


@blueprint.route("/passkey", methods=["POST"])
def passkey_create():
    """Passkey CREATE"""

    passkey_uuid = uuid.uuid4()
    torrent = request.json.get("torrent")
    user = request.json.get("user")

    passkey = PassKey(passkey_uuid, torrent, user)

    if database.add(passkey) and database.commit():
        return {
            "succes": True,
            "PassKey": {"passkey": passkey_uuid, "torrent": passkey_uuid, "user": user},
        }, 200

    return {"succes": False}, 403
