from flask import request
from utils.blueprint import Blueprint

blueprint = Blueprint("user_create")


@blueprint.route("/user", methods=["POST"])
def user_create():
    """User CREATE"""
    return {"method": "POST", "body": request.json}
