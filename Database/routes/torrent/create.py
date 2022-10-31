from flask import request
from models.torrent import Torrent
from datetime import date
from utils.blueprint import Blueprint
from utils.response import Response
from utils.sqlalchemy import SQLAlchemy

blueprint = Blueprint("torrent_create")

database: SQLAlchemy = SQLAlchemy()


@blueprint.route("/torrent", methods=["POST"])
def torrent_create():
    """Torrent CREATE"""

    current_date = date.today()

    uploader = request.json.get("uploader", False)
    info_hash = request.json.get("info_hash", False)
    name = request.json.get("name", False)
    desc = request.json.get("desc", False)
    torrent_file = request.json.get("torrent_file", False)
    torrent_version = request.json.get("torrent_version", False)
    uploaded_time = current_date
    seeders, leechers, download_count = 0, 0, 0
    last_checked = current_date

    if (
        uploader
        and info_hash
        and name
        and desc
        and torrent_file
        and torrent_version
    ):
        if not (database.query("Torrent").filter_by(info_hash=info_hash).limit(1).first()):
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
                last_checked=last_checked
            )

            if database.add(torrent) and database.commit():
                return Response.success(message="Torrent created successfully.")

        return Response.error(message="Torrent unavailable.")

    return Response.error(message="Error during torrent creation.")
