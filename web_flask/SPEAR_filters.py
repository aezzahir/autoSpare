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


@app.route("/SPEAR_filters", strict_slashes=False)
def SPEAR_filters():
    """
    displays all products
    """
    list_products = storage.all(Spear).values()
    return render_template("index.html", products=list_products)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)