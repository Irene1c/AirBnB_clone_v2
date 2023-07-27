#!/usr/bin/python3
"""script that starts a Flask web application"""
from flask import Flask, render_template
from models.state import State
from models import storage


app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def states_list():
    """display a HTML page inside body tag te States sorted by name,
        in the format: <state.id>: <B><state.name>
    """

    states = storage.all(State)
    return render_template('7-states_list.html', states=states)


@app.teardown_appcontext
def remove_session(exception=None):
    """remove the current SQLAlchemy Session after each request"""

    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
