from flask_blog import app
from flask import redirect, render_template, request, url_for, session

from author.form import RegisterForm, LoginForm

from author.models import Author

@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    data = request.form
    error = None

    username = data.get('username')
    password = data.get('password')

    if form.validate_on_submit():
        author = Author.query.filter_by(
            username=username,
            password=password
        ).limit(1)

        if author.count():
            session['username'] = username
            return(redirect(url_for('login_success')))

    return render_template("author/login.html", form=form, error=error)

@app.route("/register", methods=["GET", "POST"])
def register():

    form = RegisterForm()
    data = request.form

    if form.validate_on_submit():
        return redirect(url_for('success'))

    return render_template('author/register.html', form=form)

@app.route("/success")
def success():
    return 'Success!'

@app.route('/login_success')
def login_success():
    return 'login_success'
