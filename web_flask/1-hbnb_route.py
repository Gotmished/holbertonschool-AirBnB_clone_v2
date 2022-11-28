#!/usr/bin/python3
"""
A script to start a Flask web application that prints
one of two messages depending on the route
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


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
