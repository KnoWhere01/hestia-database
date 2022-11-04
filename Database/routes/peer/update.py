from html import escape

from flask import request

from utils.blueprint import Blueprint
from utils.response import Response
from utils.sqlalchemy import SQLAlchemy

blueprint = Blueprint("peer_update")

database: SQLAlchemy = SQLAlchemy()


@blueprint.route("/peer/<peer_id>", methods=["PATCH", "PUT"])
def peer_update(peer_id):
    """Peer UPDATE"""
    if peer_id := escape(peer_id):
        if peer := database.query("Peer").filter_by(peer_id=peer_id):
            ip = request.json.get("ip", False)
            port = request.json.get("port", False)
            uploaded = request.json.get("uploaded", False)
            downloaded = request.json.get("downloaded", False)
            left = request.json.get("left", False)
            event = request.json.get("event", False)
            tracker_id = request.json.get("tracker_id", False)
            compact = request.json.get("compact", False)
            key = request.json.get("key", False)
            corrupt = request.json.get("corrupt", False)
            no_peer_id = request.json.get("no_peer_id", False)
            user_agent = request.json.get("user_agent", False)
            

            if ip:
                peer.update({"ip": ip})

            if port:
                peer.update({"port": port})

            if uploaded:
                peer.update({"uploaded": uploaded})

            if downloaded:
                peer.update({"downloaded": downloaded})

            if left:
                peer.update({"left": left})

            if event:
                peer.update({"event": event})

            if tracker_id:
                peer.update({"tracker_id": tracker_id})

            if compact:
                peer.update({"compact": compact})

            if key:
                peer.update({"key": key})

            if corrupt:
                peer.update({"corrupt": corrupt})

            if no_peer_id:
                peer.update({"no_peer_id": no_peer_id})

            if user_agent:
                peer.update({"user_agent": user_agent})

            if database.commit():
                peer = peer.limit(1).first()

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

    return Response.error(message="Error during peer update.")
