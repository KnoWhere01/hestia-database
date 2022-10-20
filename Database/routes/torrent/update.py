from utils.blueprint import Blueprint

blueprint = Blueprint("torrent_update")


@blueprint.route("/torrent/<torrent>", methods=["PATCH", "PUT"])
def torrent_update(torrent):
    """Torrent UPDATE"""
    return {"method": ["PATCH", "PUT"], "return": torrent}
