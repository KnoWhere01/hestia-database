from html import escape

from utils.models import Peer
from utils.blueprint import Blueprint
from utils.response import Response
from utils.security import requires_api_key
from utils.sqlalchemy import SQLAlchemy

blueprint = Blueprint("peer_read")

database: SQLAlchemy = SQLAlchemy()


@blueprint.route("/peer/<peer_id>", methods=["GET"])
@requires_api_key
def peer_read(peer_id):
    """Peer READ"""

    if peer_id := escape(peer_id):
        if peer := database.query(Peer).filter_by(peer_id=peer_id).limit(1).first():
            return Response.success(
                message={
                    "torrent": peer.torrent,
                    "peer_id": peer_id,
                    "ip": peer.ip,
                    "port": peer.port,
                    "active": peer.active,
                    "uploaded": peer.uploaded,
                    "downloaded": peer.downloaded,
                    "left": peer.left,
                    "event": peer.event,
                    "tracker_id": peer.tracker_id,
                    "compact": peer.compact,
                    "key": peer.key,
                    "corrupt": peer.corrupt,
                    "no_peer_id": peer.no_peer_id,
                    "user_agent": peer.user_agent,
                }
            )

        return Response.error(message="Peer unavailable.")

    return Response.error(message="Peer unavailable.")


@blueprint.route("/peers/<torrent_id>", methods=["GET"])
@requires_api_key
def peers_read(torrent_id):
    """Peers READ"""

    if torrent_id := escape(torrent_id):
        query = database.query(Peer).filter_by(torrent_id=torrent_id)
        if peers := query.all():
            data = [peer.to_dict() for peer in peers]
            return Response.success(message=data)

        return Response.error(message="Peers unavailable.")

    return Response.error(message="Peers unavailable.")