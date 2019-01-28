from flask import Blueprint


bp = Blueprint('reservations', __name__, url_prefix='/reservations')


@bp.route('/settings_page')
def base():
    """
    @todo #32:30min Continue implementing Settings page
    """
    return 'Settings page'
