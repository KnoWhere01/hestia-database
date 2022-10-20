from utils.blueprint import Blueprint

blueprint = Blueprint("user_read")


@blueprint.route("/user/<user>", methods=["GET"])
def user_read(user):
    """User READ"""
    return {"method": "GET", "return": user}
