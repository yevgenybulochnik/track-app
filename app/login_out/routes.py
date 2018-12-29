from flask import (
    render_template,
    flash,
    redirect,
    url_for,
    request
)
from flask_login import (
    current_user,
    login_user,
    logout_user
)
from werkzeug.urls import url_parse
from app.login_out import bp
from app.login_out.forms import LoginForm
from app.models import User

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
            return redirect(url_for('login_out.login'))
        login_user(user)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('main.index')
        return redirect(urllib.parse.unquote_plus(next_page))
    return render_template('login.html', form=form)


@bp.route('/logout')
def logout():
    print(current_user.email)
    logout_user()
    return redirect(url_for('main.index'))
