from flask import request

from utils.blueprint import Blueprint
from utils.response import Response
from utils.sqlalchemy import SQLAlchemy

from html import escape

blueprint = Blueprint("torrent_read")

database: SQLAlchemy = SQLAlchemy()


@blueprint.route("/torrent/<info_hash>", methods=["GET"])
def torrent_read(info_hash):
    """Torrent READ"""

    if info_hash := escape(info_hash):
        if torrent := database.query("Torrent").filter_by(info_hash=info_hash).limit(1).first():
            return Response.success(
                message={
                    "uploader": torrent.uploader,
                    "info_hash": torrent.info_hash,
                    "name": torrent.name,
                    "desc": torrent.desc,
                    "torrent_file": torrent.torrent_file,
                    "torrent_version": torrent.torrent_version,
                    "uploaded_time": torrent.uploaded_time,
                    "download_count": torrent.download_count,
                    "seeders": torrent.seeders,
                    "leechers": torrent.leechers,
                    "last_checked": torrent.last_checked,
                }
            )

        return Response.error(message="Torrent unavailable.")

    return Response.error(message="Torrent unavailable.")
