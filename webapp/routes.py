from flask import render_template, flash, redirect, url_for, request
from webapp import app, db
from webapp.forms import LoginForm, RegistrationForm
from werkzeug.urls import url_parse
from webapp.models import User
from flask_login import current_user, login_user, logout_user, login_required

@app.route('/')
@app.route('/index')
@login_required
def index():
    posts = [
            {
        'author': {'username': 'Karolinka'},
        'body': 'Kupiłam nowy telefon i będę robić świetne zdjęcia!'
            }
    ]
    return render_template('index.html', title='Hello App', posts=posts)


@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('You are now a registered user!')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        # first and filter_by are methods of SQLAlchemy
        # filter_by returns list of usernames
        if user is None or not user.check_password(form.password.data):
        #this checks for proper user and password
            flash('Invalid username or password!')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('index')
        return redirect(next_page)
    return render_template('login.html', title = "Sign In", form=form)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))
