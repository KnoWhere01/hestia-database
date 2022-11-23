import calendar
import datetime

import jwt
from flask import request
from passlib.hash import bcrypt

from utils.models import Password, User
from utils.blueprint import Blueprint
from utils.config import config
from utils.response import Response
from utils.security import requires_api_key
from utils.sqlalchemy import SQLAlchemy

blueprint = Blueprint("password_read")

database: SQLAlchemy = SQLAlchemy()


@blueprint.route("/password", methods=["POST"])
@requires_api_key
def passkey_read():
    """Password READ"""

    username = request.json.get("username", False)
    password = request.json.get("password", False)

    if username and password:
        if user := database.query(User).filter_by(username=username).limit(1).first():
            if (
                auth := database.query(Password)
                .filter_by(user=user.id)
                .limit(1)
                .first()
            ):
                if bcrypt.verify(password, auth.password):
                    expiry = int(
                        calendar.timegm(datetime.datetime.now().timetuple())
                        + datetime.timedelta(minutes=5).total_seconds()
                    )

                    token = jwt.encode(
                        headers={"little snoop": "you don't belong here"},
                        payload={
                            "username": user.username,
                            "api_key": user.api_key,
                            "expiry": expiry,
                        },
                        key=config["JWT-SECRET"],
                        algorithm="HS256",
                    )

                    return Response.success(message={"token": token, "expiry": expiry})

                return Response.error(message="Incorrect password.")

            return Response.error(message="Incorrect password.")

        return Response.error(message="Incorrect username.")

    return Response.error(message="Bad Request.")
