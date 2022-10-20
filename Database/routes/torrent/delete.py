from utils.blueprint import Blueprint

blueprint = Blueprint("torrent_delete")


@blueprint.route("/torrent/<torrent>", methods=["DELETE"])
def torrent_delete(torrent):
    """Torrent DELETE"""
    return {"method": "DELETE", "delete": torrent}
