from html import escape

from flask import request
from passlib.hash import bcrypt

from utils.blueprint import Blueprint
from utils.response import Response
from utils.sqlalchemy import SQLAlchemy

from utils.security import requires_api_key

blueprint = Blueprint("user_update")

database: SQLAlchemy = SQLAlchemy()


@blueprint.route("/user/<user>", methods=["PATCH", "PUT"])
@requires_api_key
def user_update(user):
    """User UPDATE"""
    if username := escape(user):
        if user := database.query("User").filter_by(username=username):
            api_key = request.json.get("api_key", False)
            password = request.json.get("password", False)
            uploaded = request.json.get("uploaded", 0)
            downloaded = request.json.get("downloaded", 0)

            if api_key:
                user.update({"api_key": api_key})

            if password:
                user_query = user.limit(1).first()
                if password_query := database.query("Password").filter_by(user=user_query.id):
                    password_query.update({"password": bcrypt.hash(password)})

            if uploaded:
                user.update({"uploaded": uploaded})

            if downloaded:
                user.update({"downloaded": downloaded})

            if database.commit():
                user = user.limit(1).first()

                return Response.success(
                    message={
                        "username": user.username,
                        "uploaded": user.uploaded,
                        "downloaded": user.downloaded,
                    }
                )

        return Response.error(message="Username unavailable.")

    return Response.error(message="Error during account update.")
