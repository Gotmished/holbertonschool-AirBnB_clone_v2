#!/usr/bin/python3
"""
A script to start a Flask web application that prints
one of four messages depending on the route
"""

from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello():
    """Displaying text when calling route"""
    return ("Hello HBNB!")


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """Displaying text when calling route"""
    return ("HBNB")


@app.route("/c/<text>", strict_slashes=False)
def new_text(text):
    """Displaying text based upon user input when calling route"""
    return ("C {}".format(text.replace("_", " ")))


@app.route("/python/", strict_slashes=False, defaults={"text": "is cool"})
@app.route("/python/<text>", strict_slashes=False)
def python_text(text):
    """Displaying text when calling Python route"""
    return ("Python {}".format(text.replace("_", " ")))


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
