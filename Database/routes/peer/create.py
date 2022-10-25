from flask import request

from models.peer import Peer
from utils.blueprint import Blueprint
from utils.sqlalchemy import SQLAlchemy

blueprint = Blueprint("peer_create")

database: SQLAlchemy = SQLAlchemy()


@blueprint.route("/peer", methods=["POST"])
def peer_create():
    """Peer CREATE"""

    torrent = request.json.get("torrent")
    peer_id = request.json.get("peer_id")
    ip = request.json.get("ip")
    port = request.json.get("port")
    uploaded = request.json.get("uploaded")
    downloaded = request.json.get("downloaded")
    left = request.json.get("left")
    event = request.json.get("event")
    tracker_id = request.json.get("tracker_id")
    compact = request.json.get("compact")
    key = request.json.get("key")
    corrupt = request.json.get("corrupt")
    no_peer_id = request.json.get("no_peer_id")
    user_agent = request.json.get("user_agent")

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
        return {
            "succes": True,
            "peer": "",
        }, 200

    return {"succes": False}, 403
