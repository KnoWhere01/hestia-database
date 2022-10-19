from flask import Blueprint, request

blueprint = Blueprint(
    "user",
    __name__,
)


@blueprint.route("/user", methods=["POST"])
def user_create():
    """User CREATE"""
    return {"method": "POST", "body": request.json}


@blueprint.route("/user/<user>", methods=["GET"])
def user_read(user):
    """User READ"""
    return {"method": "GET", "return": user}


@blueprint.route("/user/<user>", methods=["PATCH", "PUT"])
def user_update(user):
    """User UPDATE"""
    return {"method": ["PATCH", "PUT"], "return": user}


@blueprint.route("/user/<user>", methods=["DELETE"])
def user_delete(user):
    """User DELETE"""
    return {"method": "GET", "delete": user}
