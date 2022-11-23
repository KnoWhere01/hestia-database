from flask import request

from utils.models import Peer
from utils.blueprint import Blueprint
from utils.response import Response
from utils.security import requires_api_key
from utils.sqlalchemy import SQLAlchemy

blueprint = Blueprint("peer_create")

database: SQLAlchemy = SQLAlchemy()


@blueprint.route("/peer", methods=["POST"])
@requires_api_key
def peer_create():
    """Peer CREATE"""

    torrent = request.json.get("torrent", False)
    peer_id = request.json.get("peer_id", False)
    ip = request.json.get("ip", False)
    port = request.json.get("port", False)
    uploaded, downloaded, uploaded_total, downloaded_total = 0, 0, 0, 0
    seeding = request.json.get("tracker_id", False)
    user_agent = request.json.get("user_agent", False)

    if (
        torrent
        and peer_id
        and ip
        and port
        and seeding
        and user_agent
    ):
        if not (database.query(Peer).filter_by(peer_id=peer_id).limit(1).first()):
            peer = Peer(
                torrent=torrent,
                peer_id=peer_id,
                ip=ip,
                port=port,
                uploaded=uploaded,
                downloaded=downloaded,
                uploaded_total=uploaded_total,
                downloaded_total=downloaded_total,
                user_agent=user_agent,
            )

            if database.add(peer) and database.commit():
                return Response.success(message="Peer created successfully.")

        return Response.error(message="Peer unavailable.")

    return Response.error(message="Error during peer creation.")
