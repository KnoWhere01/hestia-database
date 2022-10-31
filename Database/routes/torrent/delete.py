from flask import request

from utils.blueprint import Blueprint
from utils.response import Response
from utils.sqlalchemy import SQLAlchemy

blueprint = Blueprint("torrent_delete")

database: SQLAlchemy = SQLAlchemy()


@blueprint.route("/torrent", methods=["DELETE"])
def torrent_delete():
    """Torrent DELETE"""

    if info_hash := request.json.get("info_hash", False):
        if torrent := database.query("Torrent").filter_by(info_hash=info_hash):
            if torrent.delete() and database.commit():
                return Response.success(message="Torrent successfully deleted.")

            return Response.error(message="Error during torrent deletion.")

        return Response.error(message="Torrent unavailable.")

    return Response.error(message="Error during torrent deletion.")
