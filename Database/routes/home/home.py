from flask import Blueprint

blueprint = Blueprint(
    "home",
    __name__,
)


@blueprint.route("/", methods=["GET"])
def home():
    """Homepage."""
    return {}
