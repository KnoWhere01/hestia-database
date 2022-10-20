from utils.blueprint import Blueprint

blueprint = Blueprint("peer_update")


@blueprint.route("/peer/<peer>", methods=["PATCH", "PUT"])
def peer_update(peer):
    """Peer UPDATE"""
    return {"method": ["PATCH", "PUT"], "return": peer}
