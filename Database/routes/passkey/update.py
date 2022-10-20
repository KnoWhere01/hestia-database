from utils.blueprint import Blueprint

blueprint = Blueprint("passkey_update")


@blueprint.route("/passkey/<passKey>", methods=["PATCH", "PUT"])
def passkey_update(passKey):
    """Passkey UPDATE"""
    return {"method": ["PATCH", "PUT"], "return": passKey}
