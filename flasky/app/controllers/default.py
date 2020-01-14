from flask import render_template, flash, url_for
from flask_login import login_user
from werkzeug.utils import redirect

from app import app, db

from app.models.tables import User
from app.models.forms import LoginForm

@app.route('/index')
@app.route('/')
def index():
    return render_template('index.html')


@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()

    user = User.query.filter_by(username=form.username.data).first()
    if user and user.password == form.password.data:
        login_user(user)
        return redirect(url_for("index"))
    else:
        flash("Invalid login.")
    return render_template('login.html',
                           form=form)