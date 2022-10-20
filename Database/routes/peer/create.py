from flask import request
from utils.blueprint import Blueprint

blueprint = Blueprint("peer_create")


@blueprint.route("/peer", methods=["POST"])
def peer_create():
    """Peer CREATE"""
    return {"method": "POST", "body": request.json}
