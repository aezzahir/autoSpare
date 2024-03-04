#!/usr/bin/python3
"""script that starts a Flask web application"""
from models import storage
from models.spear import Spear  # Import the Spear class
from models.supplier import Supplier
from models.user import User
from models.forms import RegisterForm, LoginForm
from flask import Flask, render_template, url_for, redirect, flash
from flask_login import LoginManager, login_user, UserMixin, logout_user


app = Flask(__name__)
app.config['SECRET_KEY'] = '34d9d93fd27e9261da3cd588'
login_manager = LoginManager(app)

@login_manager.user_loader
def load_user(user_id):
    storage.reload()
    session = storage.get_session()
    return session.query(User).filter_by(id=user_id).first()


@app.teardown_appcontext
def teardown_appcontext(exception):
    """
    calls storage.close() method
    """
    storage.close()

@app.route("/home", strict_slashes=False)
@app.route("/", strict_slashes=False)
def home_page():
    """
    displays home page
    """
    return render_template("index.html")

@app.route("/market", strict_slashes=False)
def market_page():
    """
    displays all products
    """
    list_products = storage.all(Spear).values()
    return render_template("market.html", products=list_products)

@app.route("/register", methods=['GET', 'POST'])
def register_page():
    form = RegisterForm()
    if form.validate_on_submit():
        user_to_create = User(username=form.username.data,
                              email=form.email.data,
                              password_hash=form.password1.data)
        storage.reload()
        storage.new(user_to_create)
        storage.save()
        return redirect(url_for("home_page"))
    if form.errors != {}:
        for err_msg in form.errors.values():
            flash(f'There was an error with creating a user: {err_msg}', category='danger')
    return render_template('register.html', form=form)


@app.route("/login", methods=['GET', 'POST'])
def login_page():
    form = LoginForm()
    if form.validate_on_submit():
        storage.reload()
        session = storage.get_session()
        attempted_user = session.query(User).filter_by(username=form.username.data).first()
        if attempted_user and attempted_user.password_hash == form.password.data:
            login_user(attempted_user)
            flash("Succes !", category='success')
            return redirect(url_for("market_page"))
        else:
            flash("Username and password are not matched! try again", category='danger')


    return render_template('login.html', form=form)

@app.route("/logout", strict_slashes=False)
def logout_page():
    logout_user()
    flash("yo have been log out!", category='info')
    return redirect(url_for("home_page"))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)