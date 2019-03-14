import json
from flask import render_template, request, redirect, url_for
from flask_login import login_required, current_user
from app.climbing import bp
from app.climbing.models import Session, Route
from app import db


@bp.route('/dashboard', methods=['GET'])
@login_required
def dashboard():
    return render_template('climbing/dashboard.html')


@bp.route('/ropes', methods=['GET'])
@login_required
def ropesForm():
    return render_template('climbing/ropesForm.html')


@bp.route('/boulder', methods=['GET'])
@login_required
def boulderForm():
    return render_template('climbing/boulderForm.html')
