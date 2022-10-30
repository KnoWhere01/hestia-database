from flask import request
from utils.blueprint import Blueprint
from utils.response import Response
from utils.sqlalchemy import SQLAlchemy

blueprint = Blueprint("passkey_delete")

database: SQLAlchemy = SQLAlchemy()


@blueprint.route("/passkey", methods=["DELETE"])
def user_delete():
    """User DELETE"""

    if passkey := request.json.get("passkey", False):
        if passkey := database.query("PassKey").filter_by(passkey=passkey):
            if passkey.delete() and database.commit():
                return Response.success(message="Passkey successfully deleted.")

            return Response.error(message="Error during passkey deletion.")

        return Response.error(message="Passkey unavailable.")

    return Response.error(message="Error during account deletion.")
