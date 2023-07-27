#!/usr/bin/python3
"""script that starts a Flask web application"""
from flask import Flask, render_template
from models.state import State
from models import storage


app = Flask(__name__)


@app.route('/cities_by_states', strict_slashes=False)
def cities_by_states():
    """display a HTML page inside body tag te States sorted by name,
        in the format: <state.id>: <B><state.name></B>
        + UL tag: with the list of City objects linked
        to the State sorted by name in the format:
        <city.id>: <B><city.name></B>
    """

    states = storage.all(State)
    return render_template('8-cities_by_states.html', states=states)


@app.teardown_appcontext
def remove_session(exception=None):
    """remove the current SQLAlchemy Session after each request"""

    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)