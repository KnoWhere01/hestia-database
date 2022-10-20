from utils.blueprint import Blueprint

blueprint = Blueprint("user_delete")


@blueprint.route("/user/<user>", methods=["DELETE"])
def user_delete(user):
    """User DELETE"""
    return {"method": "DELETE", "delete": user}
