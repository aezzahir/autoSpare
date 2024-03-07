#!/usr/bin/python3
"""script that starts a Flask web application"""
from models import storage
from models.spear import Spear  # Import the Spear class
from models.supplier import Supplier
from models.user import User
from models.forms import RegisterForm, LoginForm, PurchaseItemForm, RemoveItemForm
from flask import Flask, render_template, url_for, redirect, flash, request
from flask_login import LoginManager, login_user, UserMixin, logout_user, login_required, current_user


app = Flask(__name__)
app.config['SECRET_KEY'] = '34d9d93fd27e9261da3cd588'
login_manager = LoginManager(app)
login_manager.login_view = "login_page"
login_manager.login_message_category = "info"

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

@app.route("/market", methods=['GET', 'POST'], strict_slashes=False)
@login_required
def market_page():
    """
    Displays all products and handles purchase requests
    """
    purchase_form = PurchaseItemForm()
    removing_form = RemoveItemForm()
    
    if request.method == "POST":
        #purchase logic
        purchased_item_id = request.form.get('purchased_item')
        purchased_item = storage.get_session().query(Spear).filter_by(id=purchased_item_id).first()
        
        if purchased_item:
            print(f"The user {current_user.username} purchased {purchased_item.designation}")
            current_user.purchased_items.append(purchased_item)
            storage.save()  # Save the changes to the database
            flash(f"Congratulations {current_user.username} for purchasing {purchased_item.designation}", category='success')
        #remove logic
        removed_item_id = request.form.get('removed_item')
        removed_item = storage.get_session().query(Spear).filter_by(id=removed_item_id).first()
        if removed_item:
            print(f"The user {current_user.username} removed {removed_item.designation}")
            current_user.purchased_items.remove(removed_item)
            storage.save()  # Save the changes to the database
            flash(f"Congratulations {current_user.username} for removing {removed_item.designation}", category='success')

        # Redirect to avoid re-submitting form data on refresh
        return redirect(url_for('market_page'))

    if request.method == "GET":
        list_products = storage.all(Spear).values()
        purchased_items = current_user.purchased_items
        return render_template("market.html", products=list_products, purchase_form=purchase_form, purchased_items=purchased_items, removing_form=removing_form)


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
        login_user(user_to_create)
        flash("Account created successfuly! You are now logged in", category='success')
        return redirect(url_for("market_page"))
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