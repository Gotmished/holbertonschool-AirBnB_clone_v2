#!/usr/bin/python3
"""
Script to begin a Flask web application.
Application listening on 0.0.0.0, port 5000
"""

from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """Displaying text when calling route"""
    return ("Hello HBNB!")


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
