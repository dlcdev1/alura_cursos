from flask import render_template
from app import app
from app.models.forms import LoginForm

@app.route('/index')
@app.route('/')
def index():
    return render_template('index.html')

@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        print(form.username.data)
        print(form.password.data)
    return render_template('login.html',
                           form=form)