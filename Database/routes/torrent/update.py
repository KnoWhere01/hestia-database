from html import escape

from flask import request

from models.torrent import Torrent
from utils.blueprint import Blueprint
from utils.response import Response
from utils.security import requires_api_key
from utils.sqlalchemy import SQLAlchemy

blueprint = Blueprint("torrent_update")

database: SQLAlchemy = SQLAlchemy()


@blueprint.route("/torrent/<info_hash>", methods=["PATCH", "PUT"])
@requires_api_key
def torrent_update(info_hash):
    """Torrent UPDATE"""
    if info_hash := escape(info_hash):
        if torrent := database.query(Torrent).filter_by(info_hash=info_hash):
            uploader = request.json.get("uploader", False)
            name = request.json.get("name", False)
            desc = request.json.get("desc", False)
            torrent_file = request.json.get("torrent_file", False)
            version = request.json.get("version", False)
            uploaded_time = request.json.get("uploaded_time", False)
            download_count = request.json.get("download_count", False)
            seeders = request.json.get("seeders", False)
            leechers = request.json.get("leechers", False)
            last_checked = request.json.get("last_checked", False)

            if uploader:
                torrent.update({"uploader": uploader})

            if name:
                torrent.update({"name": name})

            if desc:
                torrent.update({"desc": desc})

            if torrent_file:
                torrent.update({"torrent_file": torrent_file})

            if version:
                torrent.update({"version": version})

            if uploaded_time:
                torrent.update({"uploaded_time": uploaded_time})

            if download_count:
                torrent.update({"download_count": download_count})

            if seeders:
                torrent.update({"seeders": seeders})

            if leechers:
                torrent.update({"leechers": leechers})

            if last_checked:
                torrent.update({"last_checked": last_checked})

            if database.commit():
                torrent = torrent.limit(1).first()

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

    return Response.error(message="Error during torrent update.")
