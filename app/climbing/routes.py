from flask import render_template
from flask_login import login_required, current_user
from app.climbing import bp


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
    return render_template('climbing/session.html', props=test_props)
