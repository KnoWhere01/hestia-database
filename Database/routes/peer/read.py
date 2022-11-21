from utils.blueprint import Blueprint
from utils.response import Response
from utils.sqlalchemy import SQLAlchemy

from models.peer import Peer

from html import escape

from utils.security import requires_api_key

blueprint = Blueprint("peer_read")

database: SQLAlchemy = SQLAlchemy()


@blueprint.route("/peer/<peer_id>", methods=["GET"])
@requires_api_key
def torrent_read(peer_id):
    """Peer READ"""

    if peer_id := escape(peer_id):
        if peer := database.query(Peer).filter_by(peer_id=peer_id).limit(1).first():
            return Response.success(
                message={
                    "torrent": peer.torrent,
                    "peer_id": peer_id,
                    "ip": peer.ip,
                    "port": peer.port,
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
