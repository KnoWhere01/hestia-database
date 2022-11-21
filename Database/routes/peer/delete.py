from flask import request

from utils.blueprint import Blueprint
from utils.response import Response
from utils.sqlalchemy import SQLAlchemy

from models.peer import Peer

from utils.security import requires_api_key

blueprint = Blueprint("peer_delete")

database: SQLAlchemy = SQLAlchemy()


@blueprint.route("/peer", methods=["DELETE"])
@requires_api_key
def peer_delete():
    """Peer DELETE"""

    if peer_id := request.json.get("peer_id", False):
        if peer := database.query(Peer).filter_by(peer_id=peer_id):
            if peer.delete() and database.commit():
                return Response.success(message="Peer successfully deleted.")

            return Response.error(message="Error during peer deletion.")

        return Response.error(message="Peer unavailable.")

    return Response.error(message="Error during peer deletion.")
