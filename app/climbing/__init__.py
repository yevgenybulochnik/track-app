from flask import Blueprint


bp = Blueprint(
    'climbing', __name__,
    template_folder='templates',
    static_folder='static',
    static_url_path='/static/climbing'
)

from app.climbing import routes
