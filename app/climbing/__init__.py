from flask import Blueprint


bp = Blueprint(
    'climbing', __name__,
    template_folder='templates',
)

from app.climbing import routes
