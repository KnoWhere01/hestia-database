from flask import request
from models.peer import Peer
from utils.blueprint import Blueprint
from utils.response import Response
from utils.sqlalchemy import SQLAlchemy

blueprint = Blueprint("peer_create")

database: SQLAlchemy = SQLAlchemy()


@blueprint.route("/peer", methods=["POST"])
def peer_create():
    """Peer CREATE"""

    torrent = request.json.get("torrent", False)
    peer_id = request.json.get("peer_id", False)
    ip = request.json.get("ip", False)
    port = request.json.get("port", False)
    uploaded, downloaded, left = 0, 0, 0
    event = request.json.get("event", False)
    tracker_id = request.json.get("tracker_id", False)
    compact = request.json.get("compact", False)
    key = request.json.get("key", False)
    corrupt = request.json.get("corrupt", False)
    no_peer_id = request.json.get("no_peer_id", False)
    user_agent = request.json.get("user_agent", False)

    if (
        torrent
        and peer_id
        and ip
        and port
        and event
        and tracker_id
        and compact
        and key
        and corrupt
        and no_peer_id
        and user_agent
    ):
        if not (database.query("Peer").filter_by(peer_id=peer_id).limit(1).first()):
            peer = Peer(
                torrent=torrent,
                peer_id=peer_id,
                ip=ip,
                port=port,
                uploaded=uploaded,
                downloaded=downloaded,
                left=left,
                event=event,
                tracker_id=tracker_id,
                compact=compact,
                key=key,
                corrupt=corrupt,
                no_peer_id=no_peer_id,
                user_agent=user_agent,
            )

            if database.add(peer) and database.commit():
                return Response.success(message="Peer created successfully.")

        return Response.error(message="Peer unavailable.")

    return Response.error(message="Error during peer creation.")
