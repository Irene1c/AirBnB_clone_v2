#!/usr/bin/python3
"""script that starts a Flask web application"""
from flask import Flask, render_template
from models.state import State
from models import storage


app = Flask(__name__)


@app.route('/states', strict_slashes=False)
def states():
    """display a HTML page inside body tag te States sorted by name,
        in the format: <state.id>: <B><state.name></B>
    """

    states = storage.all(State)
    return render_template('9-states.html', states=states)


@app.route('/states/<id>', strict_slashes=False)
def cities_by_states(id):
    """display a HTML page If a State object is found with this id
    """

    states = storage.all(State)
    return render_template('9-states.html', id=id, states=states)


@app.teardown_appcontext
def remove_session(exception=None):
    """remove the current SQLAlchemy Session after each request"""

    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
