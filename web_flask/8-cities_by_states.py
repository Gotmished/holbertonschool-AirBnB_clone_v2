#!/usr/bin/python3
"""
A script to start a Flask web application that fetches data
from storage, removes the current session after each request,
and displays an HTML page listing all states present
"""

from flask import Flask, render_template
from models import storage

app = Flask(__name__, template_folder='templates')


@app.teardown_appcontext
def app_teardown(exception=None):
    """Removes current session following each request"""
    storage.close()


@app.route('/cities_by_states', strict_slashes=False)
def show_cities_by_state():
    """
    Displays all cities currently in storage
    in a rendered HTML page, and arranged by state
    """
    return render_template('8-cities_by_states.html',
                           state_dict=storage.all("State"))


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
