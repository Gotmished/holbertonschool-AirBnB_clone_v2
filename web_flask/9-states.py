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


@app.route('/states', strict_slashes=False)
def show_states():
    """
    Displays all states currently in storage
    in a rendered HTML page
    """
    return render_template('7-states_list.html',
                           state_dict=storage.all("State"))


@app.route('/states/<id>', strict_slashes=False)
def show_cities_in_state(id):
    """
    Displays all cities of a particular state based upon
    supplied state id arg
    """
    city_list = []
    state_dict = storage.all("State")
    for each_state in state_dict.values():
        if each_state.id == id:
            state_name = each_state.name
            state_id = each_state.id
            for each_city in each_state.cities:
                city_details = (each_city.id, each_city.name)
                city_list.append(city_details)
    city_list.sort(key=lambda a: a[1])
    return render_template('9-states.html',
                           state_name=state_name,
                           state_id=state_id,
                           city_list=city_list
                           )


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
