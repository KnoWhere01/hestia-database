from flask import request

from utils.blueprint import Blueprint
from utils.response import Response
from utils.sqlalchemy import SQLAlchemy

from models.torrent import Torrent

from html import escape

from utils.security import requires_api_key

blueprint = Blueprint("torrent_read")

database: SQLAlchemy = SQLAlchemy()

@blueprint.route("/torrents", methods=["GET"])
@requires_api_key
def torrents_read():
    """Torrents READ"""

    page = request.args.get("page", 0)
    item = request.args.get("item", 40)

    query = database.query(Torrent)

    if page:
        query = query.offset(page*item)

    query = query.limit(item)

    if torrents := query.all():
        data = [torrent.to_dict() for torrent in torrents]
        return Response.success(message=data)        

    return Response.error(message="Torrents unavailable.")


@blueprint.route("/torrent/<info_hash>", methods=["GET"])
@requires_api_key
def torrent_read(info_hash):
    """Torrent READ"""

    if info_hash := escape(info_hash):
        if torrent := database.query(Torrent).filter_by(info_hash=info_hash).limit(1).first():
            return Response.success(
                message={
                    "uploader": torrent.uploader,
                    "info_hash": torrent.info_hash,
                    "name": torrent.name,
                    "desc": torrent.desc,
                    "torrent_file": torrent.torrent_file,
                    "version": torrent.version,
                    "uploaded_time": torrent.uploaded_time,
                    "download_count": torrent.download_count,
                    "seeders": torrent.seeders,
                    "leechers": torrent.leechers,
                    "last_checked": torrent.last_checked,
                }
            )

        return Response.error(message="Torrent unavailable.")

    return Response.error(message="Torrent unavailable.")
