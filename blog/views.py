from flask_blog import app, db
from flask import render_template, flash, url_for, request, redirect

from blog.form import SetupForm

from author.models import Author
from blog.models import Blog

from author.decorators import login_required

@app.route("/")
@app.route("/index")
def index():
    blogs = Blog.query.count()
    if blogs == 0:
        return redirect(url_for('setup'))

    return "Hello world"

@app.route("/admin")
@login_required
def admin():
    return render_template('blog/admin.html')

@app.route("/setup", methods=["GET", "POST"])
def setup():
    form = SetupForm()
    data = request.form
    error = ""

    blog_name  = data.get('name')
    username   = data.get('username')
    password   = data.get('password')
    fullname   = data.get('fullname')
    email      = data.get('email')

    print("form.validate_on_submit(): {}".format(form.validate_on_submit()))
    print("data: {}".format(data))

    if form.validate_on_submit():
        author = Author(
            password = password,
            email = email,
            fullname = fullname,
            username = username,
            is_author = True
        )

        db.session.add(author)
        db.session.flush()

        if author.id:
            blog = Blog(
                admin = author.id,
                name = blog_name
            )
            db.session.add(blog)
            db.session.flush()
        else:
            db.session.rollback()
            error = "Error creating Author"

        if author.id and blog.id:
            db.session.commit()
            flash("Blog created")
            return redirect(url_for("admin"))
        else:
            db.session.rollback()
            error = "Error creating Blog"

    return render_template('blog/setup.html', form=form, error=error)
