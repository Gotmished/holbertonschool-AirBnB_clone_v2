#!/usr/bin/python3
"""
A script to start a Flask web application that fetches data
from storage, removes the current session after each request,
and displays an hbnb webpage
"""

from flask import Flask, render_template
from models import storage

app = Flask(__name__, template_folder='templates')


@app.teardown_appcontext
def app_teardown(exception=None):
    """Removes current session following each request"""
    storage.close()


@app.route('/hbnb_filters', strict_slashes=False)
def hbnb_filters():
    """
    Displays states, cities, and amenities on
    the hbnb webpage
    """
    state_dict = storage.all('State')
    amenity_dict = storage.all('Amenity')
    return render_template('10-hbnb_filters.html',
                           state_dict=state_dict,
                           amenity_dict=amenity_dict
                           )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
