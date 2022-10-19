from flask import Blueprint, request

blueprint = Blueprint(
    "passkey",
    __name__,
)


@blueprint.route("/passkey", methods=["POST"])
def passkey_create():
    """Passkey CREATE"""
    return {"method": "POST", "body": request.json}


@blueprint.route("/passkey/<passKey>", methods=["GET"])
def passkey_read(passKey):
    """Passkey READ"""
    return {"method": "GET", "return": passKey}


@blueprint.route("/passkey/<passKey>", methods=["PATCH", "PUT"])
def passkey_update(passKey):
    """Passkey UPDATE"""
    return {"method": ["PATCH", "PUT"], "return": passKey}


@blueprint.route("/passkey/<passKey>", methods=["DELETE"])
def passkey_delete(passKey):
    """Passkey DELETE"""
    return {"method": "GET", "delete": passKey}
