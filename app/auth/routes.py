from flask import (
    render_template,
    flash,
    redirect,
    url_for,
    request,
    jsonify
)
from flask_login import (
    current_user,
    login_user,
    logout_user,
    login_required
)
from flask_jwt_extended import create_access_token
from werkzeug.urls import url_parse
from app.auth import bp
from app.auth.forms import LoginForm
from app.main.models import User

import urllib.parse


@bp.route('/login', methods=['POST', 'GET'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user is None or not user.verify_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('auth.login'))
        login_user(user)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('main.index')
        return redirect(urllib.parse.unquote_plus(next_page))
    return render_template('auth/login.html', form=form)


@bp.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('main.index'))


@bp.route('/wctoken', methods=['POST'])
@login_required
def wctoken():
    token = create_access_token(identity=current_user.id)
    return jsonify(access_token=token)
