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
    return render_template('climbing/session.html')
