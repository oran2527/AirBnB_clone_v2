#!/usr/bin/python3
''' point 11 '''
from models import storage
from models.state import State
from models.amenity import Amenity
from flask import Flask, render_template
app = Flask(__name__, template_folder='templates')


@app.route('/', strict_slashes=False)
def index():
    '''index function'''
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    '''route hbnb function'''
    return 'HBNB'


@app.route('/c/<text>', methods=['GET'], strict_slashes=False)
def cplussomething(text):
    '''route c function'''
    var = text.replace("_", " ")
    return 'C ' + var


@app.route('/python', methods=['GET'], strict_slashes=False)
@app.route('/python/', methods=['GET'], strict_slashes=False)
@app.route('/python/<text>', methods=['GET'], strict_slashes=False)
def pythonplussomething(text=""):
    '''route python function'''
    if text == "":
        var = "is cool"
    else:
        var = text.replace("_", " ")
    return 'Python ' + var


@app.route('/number/<int:n>', methods=['GET'], strict_slashes=False)
def int_number(n):
    '''route number integer function'''
    return "{} is a number".format(n)


@app.route('/number_template/<int:n>', methods=['GET'], strict_slashes=False)
def int_template(n):
    '''route number_template integer function'''
    return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>', methods=['GET\
'], strict_slashes=False)
def int_odd_even_template(n):
    '''route number_odd_even_template integer function'''
    if n % 2 == 0:
        eo = 'even'
    else:
        eo = 'odd'
    return render_template('6-number_odd_or_even.html', n=n, eo=eo)


@app.route('/states_list', strict_slashes=False)
def list_state():
    '''route list state function'''
    return render_template('7-states_list.html\
', states=storage.all(State).values())


@app.teardown_appcontext
def ses_close(response_or_exc):
    '''close session'''
    storage.close()


@app.route('/cities_by_states', strict_slashes=False)
def list_cities_state():
    '''route list cities state function'''
    return render_template('8-cities_by_states.html\
', states=storage.all(State).values())


@app.route('/states/<text>', methods=['GET'], strict_slashes=False)
@app.route('/states', strict_slashes=False)
def list_cities_state_cond(text=""):
    '''route list cities state conditionals function'''
    if text == "":
        return render_template('9-states.html\
', states=storage.all(State).values(), flag=1)
    else:
        states = storage.all(State).values()
        st = None
        for state in states:
            if state.id == text:
                st = state
        if st:
            return render_template('9-states.html\
', st=st, flag=2)
        else:
            return render_template('9-states.html\
', nf='Not found!', flag=3)


@app.route('/hbnb_filters', strict_slashes=False)
def hbnb_template():
    '''route hbnb_template function'''
    return render_template('10-hbnb_filters.html\
', states=storage.all(State).values(),\
amenities=storage.all(Amenity).values())


if __name__ == '__main__':
    app.run(host="0.0.0.0", port="5000")
