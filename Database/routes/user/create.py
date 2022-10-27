from flask import request
from passlib.hash import bcrypt

from models.user import User
from utils.blueprint import Blueprint
from utils.response import Response
from utils.sqlalchemy import SQLAlchemy

blueprint = Blueprint("user_create")

database: SQLAlchemy = SQLAlchemy()


@blueprint.route("/user", methods=["POST"])
def user_create():
    """User CREATE"""

    username = request.json.get("username", False)
    password = request.json.get("password", False)
    uploaded, downloaded = 0, 0

    if username and password:
        if not (database.query("User").filter_by(username=username).limit(1).first()):
            user = User(
                username=username,
                password=bcrypt.hash(password),
                uploaded=uploaded,
                downloaded=downloaded,
            )

            if database.add(user) and database.commit():
                return Response.success(message="Account created successfully.")

        return Response.error(message="Username unavailable.")

    return Response.error(message="Error during account creation.")
