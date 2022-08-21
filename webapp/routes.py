from flask import render_template, flash, redirect, url_for
from webapp import app
from webapp.forms import LoginForm

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Wiktor'}
    posts = [
        {
            'author': {'username': 'Karolinka'},
            'body': 'Kupiłam nowy telefon i będę robić świetne zdjęcia!'
        }
    ]
    return render_template('index.html', title='Hello App', user=user, posts=posts)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash(f'Login requested for user {form.username.data}, '
              f'remember me = {form.remember_me.data}')
        return redirect(url_for('index'))
    return render_template('login.html', title = "Sign In", form=form)
