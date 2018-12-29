from flask import Blueprint


bp = Blueprint('login_out', __name__, template_folder='templates')

from app.login_out import routes, login
