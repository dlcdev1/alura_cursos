from flask import render_template, flash, url_for
from flask_login import login_user, logout_user
from werkzeug.utils import redirect

from app import app, db, login_manager

from app.models.tables import User
from app.models.forms import LoginForm

@login_manager.user_loader
def load_user(id):
    return User.query.filter_by(id=id).first()

@app.route('/index')
@app.route('/')
def index():
    return render_template('index.html')

@app.route("/login", methods=["GET", "POST"])
@app.route('/login')
def login():
    form = LoginForm()
    user = User.query.filter_by(username=form.username.data).first()
    if user and user.password == form.password.data:
        flash(f"User: {user.name} logado!")
        return redirect(url_for("index"))
    else:
        flash("Invalid login.")
    return render_template('login.html',
                           form=form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))