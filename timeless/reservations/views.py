from flask import Blueprint


bp = Blueprint('reservations', __name__, url_prefix='/reservations')


@bp.route('/settings')
def base():
    """
    @todo #32:30min Continue implementing Settings page
    """
    return 'Settings API entry point'
