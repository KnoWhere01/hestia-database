from flask import request
from models.user import User
from passlib.hash import bcrypt
from utils.blueprint import Blueprint
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

        user = User(
            username=username,
            password=bcrypt.hash(password),
            uploaded=uploaded,
            downloaded=downloaded,
        )

        if database.add(user) and database.commit():
            return {
                "succes": True,
                "message": "Account created successfully.",
            }, 200

    return {
        "succes": False,
        "message": "Error during account creation.",
        }, 403
