from flask import request
from utils.blueprint import Blueprint

blueprint = Blueprint("torrent_create")


@blueprint.route("/torrent", methods=["POST"])
def torrent_create():
    """Torrent CREATE"""
    return {"method": "POST", "body": request.json}
