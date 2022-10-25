from flask import request

from models.user import User
from utils.blueprint import Blueprint
from utils.sqlalchemy import SQLAlchemy

blueprint = Blueprint("user_create")

database: SQLAlchemy = SQLAlchemy()


@blueprint.route("/user", methods=["POST"])
def user_create():
    """User CREATE"""

    username = request.json.get("username")
    password = request.json.get("password")
    uploaded = 0
    downloaded = 0

    user = User(
        username=username,
        password=password,
        uploaded=uploaded,
        downloaded=downloaded,
    )

    if database.add(user) and database.commit():
        return {
            "succes": True,
            "user": {"username": username},
        }, 200

    return {"succes": False}, 403
