from flask import Blueprint, request

blueprint = Blueprint(
    "torrent",
    __name__,
)


@blueprint.route("/torrent", methods=["POST"])
def torrent_create():
    """Torrent CREATE"""
    return {"method": "POST", "body": request.json}


@blueprint.route("/torrent/<torrent>", methods=["GET"])
def torrent_read(torrent):
    """Torrent READ"""
    return {"method": "GET", "return": torrent}


@blueprint.route("/torrent/<torrent>", methods=["PATCH", "PUT"])
def torrent_update(torrent):
    """Torrent UPDATE"""
    return {"method": ["PATCH", "PUT"], "return": torrent}


@blueprint.route("/torrent/<torrent>", methods=["DELETE"])
def torrent_delete(torrent):
    """Torrent DELETE"""
    return {"method": "GET", "delete": torrent}
