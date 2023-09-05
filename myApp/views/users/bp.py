from flask import Blueprint

bp = Blueprint('users', __name__, template_folder='templates')

@bp.route('/')
def index():
    return 'This is The User Management and Login section of website'

