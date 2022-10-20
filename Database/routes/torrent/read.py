from utils.blueprint import Blueprint

blueprint = Blueprint("torrent_read")


@blueprint.route("/torrent/<torrent>", methods=["GET"])
def torrent_read(torrent):
    """Torrent READ"""
    return {"method": "GET", "return": torrent}
