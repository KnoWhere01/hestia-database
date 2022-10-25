from flask import request

from models.torrent import Torrent
from utils.blueprint import Blueprint
from utils.sqlalchemy import SQLAlchemy

blueprint = Blueprint("torrent_create")

database: SQLAlchemy = SQLAlchemy()


@blueprint.route("/torrent", methods=["POST"])
def torrent_create():
    """Torrent CREATE"""

    uploader = request.json.get("uploader")
    info_hash = request.json.get("info_hash")
    name = request.json.get("name")
    desc = request.json.get("desc")
    torrent_file = request.json.get("torrent_file")
    torrent_version = request.json.get("torrent_version")
    uploaded_time = request.json.get("uploaded_time")
    download_count = request.json.get("download_count")
    seeders = request.json.get("seeders")
    leechers = request.json.get("leechers")
    last_checked = request.json.get("last_checked")

    torrent = Torrent(
        uploader=uploader,
        info_hash=info_hash,
        name=name,
        desc=desc,
        torrent_file=torrent_file,
        torrent_version=torrent_version,
        uploaded_time=uploaded_time,
        download_count=download_count,
        seeders=seeders,
        leechers=leechers,
        last_checked=last_checked,
    )

    if database.add(torrent) and database.commit():
        return {
            "succes": True,
            "torrent": "",
        }, 200

    return {"succes": False}, 403
