from flask import request

from utils.blueprint import Blueprint
from utils.response import Response
from utils.sqlalchemy import SQLAlchemy

blueprint = Blueprint("user_delete")

database: SQLAlchemy = SQLAlchemy()


@blueprint.route("/user", methods=["DELETE"])
def user_delete():
    """User DELETE"""

    if username := request.json.get("username", False):
        if user := database.query("User").filter_by(username=username):
            if user.delete() and database.commit():
                return Response.success(message="Account successfully deleted.")

            return Response.error(message="Error during account deletion.")

        return Response.error(message="Username unavailable.")

    return Response.error(message="Error during account deletion.")
