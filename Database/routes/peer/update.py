from html import escape

from flask import request

from models.peer import Peer
from utils.blueprint import Blueprint
from utils.response import Response
from utils.security import requires_api_key
from utils.sqlalchemy import SQLAlchemy

blueprint = Blueprint("peer_update")

database: SQLAlchemy = SQLAlchemy()


@blueprint.route("/peer/<peer_id>", methods=["PATCH", "PUT"])
@requires_api_key
def peer_update(peer_id):
    """Peer UPDATE"""
    if peer_id := escape(peer_id):
        if peer := database.query(Peer).filter_by(peer_id=peer_id):
            ip = request.json.get("ip", False)
            port = request.json.get("port", False)
            uploaded = request.json.get("uploaded", False)
            downloaded = request.json.get("downloaded", False)
            uploaded_total = request.json.get("uploaded_total", False)
            downloaded_total = request.json.get("downloaded_total", False)
            seeding = request.json.get("seeding", False)
            user_agent = request.json.get("user_agent", False)

            if ip:
                peer.update({"ip": ip})

            if port:
                peer.update({"port": port})

            if uploaded:
                peer.update({"uploaded": uploaded})

            if downloaded:
                peer.update({"downloaded": downloaded})

            if uploaded_total:
                peer.update({"uploaded_total": uploaded_total})

            if downloaded_total:
                peer.update({"downloaded_total": downloaded_total})

            if seeding:
                peer.update({"seeding": seeding})

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
                        "uploaded_total": peer.uploaded_total,
                        "downloaded_total": peer.downloaded_total,
                        "seeding": peer.seeding,
                        "user_agent": peer.user_agent,
                    }
                )

        return Response.error(message="Peer unavailable.")

    return Response.error(message="Error during peer update.")
