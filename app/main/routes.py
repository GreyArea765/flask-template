from flask import current_app, render_template, url_for, flash, redirect
from flask_login import current_user, login_required
from app.main import bp
from app import db


@bp.route('/')
@bp.route('/index')
@login_required
def index():
    return render_template('index.html', title='Home')


@bp.route('/about')
@login_required
def about():
    return render_template('about.html', title='About')
