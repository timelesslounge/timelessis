from flask import Blueprint


bp = Blueprint("company", __name__, url_prefix="/companies")


@bp.route("/")
def base():
    return "Hello company"
