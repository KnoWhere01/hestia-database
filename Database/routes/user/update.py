from utils.blueprint import Blueprint

blueprint = Blueprint("user_update")


@blueprint.route("/user/<user>", methods=["PATCH", "PUT"])
def user_update(user):
    """User UPDATE"""
    return {"method": ["PATCH", "PUT"], "return": user}
