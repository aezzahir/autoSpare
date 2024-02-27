#!/usr/bin/python3
"""script that starts a Flask web application"""
from models import storage
from models.spear import Spear  # Import the Spear class
from models.supplier import Supplier
from flask import Flask, render_template

app = Flask(__name__)


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


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)