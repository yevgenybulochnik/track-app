from flask import render_template
from flask_login import login_required
from app import api
from app.main import bp
from app.main.resources import UserListResource

api.add_resource(UserListResource, '/api/users')


@bp.route('/')
@login_required
def index():
    return render_template('main/index.html')
