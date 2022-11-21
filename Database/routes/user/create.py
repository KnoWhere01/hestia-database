from flask import request

from models.user import User
from models.password import Password
from utils.blueprint import Blueprint
from utils.response import Response
from utils.sqlalchemy import SQLAlchemy

import uuid

from passlib.hash import bcrypt

from utils.security import requires_api_key

blueprint = Blueprint("user_create")

database: SQLAlchemy = SQLAlchemy()


@blueprint.route("/user", methods=["POST"])
@requires_api_key
def user_create():
    """User CREATE"""

    username = request.json.get("username", False)
    password = request.json.get("password", False)
    uploaded, downloaded = 0, 0

    if username and password:
        if not (database.query(User).filter_by(username=username).limit(1).first()):
            user = User(
                api_key=str(uuid.uuid4()),
                username=username,
                uploaded=uploaded,
                downloaded=downloaded,
            )

            if database.add(user) and database.commit():

                password = Password(user=user.id, password=bcrypt.hash(password))

                if database.add(password) and database.commit():
                    return Response.success(message="Account created successfully.")

        return Response.error(message="Username unavailable.")

    return Response.error(message="Error during account creation.")
