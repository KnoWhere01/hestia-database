import uuid

from flask import request
from models.passkey import PassKey
from utils.blueprint import Blueprint
from utils.response import Response
from utils.sqlalchemy import SQLAlchemy

from models.passkey import PassKey

from utils.security import requires_api_key

blueprint = Blueprint("passkey_create")

database: SQLAlchemy = SQLAlchemy()


@blueprint.route("/passkey", methods=["POST"])
@requires_api_key
def passkey_create():
    """Passkey CREATE"""

    passkey_uuid = uuid.uuid4()
    torrent = request.json.get("torrent", False)
    user = request.json.get("user", False)

    if passkey_uuid and torrent and user:
        if not (
            database.query(PassKey).filter_by(passkey=passkey_uuid).limit(1).first()
        ):
            passkey = PassKey(passkey=passkey_uuid, torrent=torrent, user=user)

            if database.add(passkey) and database.commit():
                return Response.success(message="PassKey created successfully.")

        return Response.error(message="PassKey unavailable.")

    return Response.error(message="Error during passkey creation.")
