#!/usr/bin/python3
"""
A script to start a Flask web application that fetches data
from storage, removes the current session after each request,
and displays an HTML page listing all states present
"""

from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__, template_folder='templates')


@app.route('/states_list', strict_slashes=False)
def show_states():
    """
    Displays all stages currently in storage
    in a rendered HTML page
    """
    return render_template('7-states_list.html',
                           state_dict=storage.all(State))


@app.teardown_appcontext
def app_teardown(exception=None):
    """Removes current session following each request"""
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
