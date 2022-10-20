from utils.blueprint import Blueprint

blueprint = Blueprint("peer_delete")


@blueprint.route("/peer/<peer>", methods=["DELETE"])
def peer_delete(peer):
    """Peer DELETE"""
    return {"method": "DELETE", "delete": peer}
