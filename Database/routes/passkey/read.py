from utils.blueprint import Blueprint

blueprint = Blueprint("passkey_read")


@blueprint.route("/passkey/<passKey>", methods=["GET"])
def passkey_read(passKey):
    """Passkey READ"""
    return {"method": "GET", "return": passKey}
