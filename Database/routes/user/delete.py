from flask import request

from utils.blueprint import Blueprint
from utils.response import Response
from utils.sqlalchemy import SQLAlchemy

from utils.security import requires_api_key

blueprint = Blueprint("user_delete")

database: SQLAlchemy = SQLAlchemy()


@blueprint.route("/user", methods=["DELETE"])
@requires_api_key
def user_delete():
    """User DELETE"""

    if username := request.json.get("username", False):
        if user := database.query("User").filter_by(username=username):
            if query_user := user.limit(1).first():
                if password := database.query("Password").filter_by(user=query_user.id):
                    if user.delete() and password.delete() and database.commit():
                        return Response.success(message="Account successfully deleted.")

            return Response.error(message="Error during account deletion.")

        return Response.error(message="Username unavailable.")

    return Response.error(message="Error during account deletion.")
