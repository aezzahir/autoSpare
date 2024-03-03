#!/usr/bin/python3
"""script that starts a Flask web application"""
from models import storage
from models.spear import Spear  # Import the Spear class
from models.supplier import Supplier
from models.user import User
from models.forms import RegisterForm
from flask import Flask, render_template, url_for, redirect, flash

app = Flask(__name__)
app.config['SECRET_KEY'] = '34d9d93fd27e9261da3cd588'


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
    displays all products
    """
    list_products = storage.all(Spear).values()
    return render_template("index.html", products=list_products)

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


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)