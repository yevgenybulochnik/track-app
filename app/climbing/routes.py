import json
from flask import render_template, request, redirect, url_for
from flask_login import login_required, current_user
from app.climbing import bp
from app.climbing.models import Session, Route
from app import db


@bp.route('/overview', methods=['GET'])
@login_required
def overview():
    return render_template('climbing/index.html')


@bp.route('/session', methods=['GET', 'POST'])
@login_required
def session():
    test_props = {
        "users": [
            {"username": current_user.email}
        ]
    }
    if request.method == 'POST':
        data = json.loads(request.data)
        routes = [Route(**route_data) for route_data in data['routes']]
        climbing_session = Session(
            type=data['session_type'],
            user=current_user,
            routes=routes
        )
        db.session.add(climbing_session)
        db.session.commit()
        return 'session saved'
    return render_template('climbing/session.html', props=test_props)
