from flask import request
from utils.blueprint import Blueprint

blueprint = Blueprint("passkey_create")


@blueprint.route("/passkey", methods=["POST"])
def passkey_create():
    """Passkey CREATE"""
    return {"method": "POST", "body": request.json}
