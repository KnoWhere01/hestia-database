from utils.blueprint import Blueprint

blueprint = Blueprint("passkey_delete")


@blueprint.route("/passkey/<passKey>", methods=["DELETE"])
def passkey_delete(passKey):
    """Passkey DELETE"""
    return {"method": "DELETE", "delete": passKey}
