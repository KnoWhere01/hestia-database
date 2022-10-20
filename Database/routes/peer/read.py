from utils.blueprint import Blueprint

blueprint = Blueprint("peer_read")


@blueprint.route("/peer/<peer>", methods=["GET"])
def peer_read(peer):
    """Peer READ"""
    return {"method": "GET", "return": peer}
