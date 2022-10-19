from flask import Blueprint, request

blueprint = Blueprint(
    "peer",
    __name__,
)


@blueprint.route("/peer", methods=["POST"])
def peer_create():
    """Peer CREATE"""
    return {"method": "POST", "body": request.json}


@blueprint.route("/peer/<peer>", methods=["GET"])
def peer_read(peer):
    """Peer READ"""
    return {"method": "GET", "return": peer}


@blueprint.route("/peer/<peer>", methods=["PATCH", "PUT"])
def peer_update(peer):
    """Peer UPDATE"""
    return {"method": ["PATCH", "PUT"], "return": peer}


@blueprint.route("/peer/<peer>", methods=["DELETE"])
def peer_delete(peer):
    """Peer DELETE"""
    return {"method": "GET", "delete": peer}
