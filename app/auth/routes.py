from flask import render_template, url_for, flash, redirect
from app import db
from app.auth.forms import LoginForm, AccountForm
from app.auth import bp
from app.dbmodels import User
from flask_login import current_user, login_user, logout_user, login_required


@bp.route('/login', methods=['GET', 'POST'])
def login():
    # Logged in users should not be logging in, send them on. (current_user
    # comes from flask_login).
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))
    
    # Instantiate a LoginForm() object
    form = LoginForm()
    if form.validate_on_submit():
        # Load user object from database using form data as the key.
        user = User.query.filter_by(username=form.username.data).first()
        # Use User class method to verify the password from form data.
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or bad password', 'danger')
            return redirect(url_for('auth.login'))
        # Login successful, invoke the Flask-Login method login_user
        login_user(user, remember=form.remember_me.data)
        # Final step is to redirect logged-in user to home page.
        return redirect(url_for('main.index'))
    return render_template('login.html', title='Log In', form=form)


@bp.route('/logout', methods=['GET', 'POST'])
def logout():
    logout_user()
    return redirect(url_for('auth.login'))


@bp.route('/account', methods=['GET', 'POST'])
@login_required
def account():
    # Instantiate a form object
   
    form = AccountForm()

    if form.validate_on_submit():
        # Verify that the user knows the current password.
        if not current_user.check_password(form.currentpassword.data):
            flash('Current password invalid', 'danger')
            return redirect(url_for('auth.account'))
        else:
            current_user.set_password(form.password.data)
            db.session.add(current_user)
            db.session.commit()
            flash('Password successfully changed', 'success')
            return redirect(url_for('main.index'))
    return render_template('account.html', title='Account', form=form)