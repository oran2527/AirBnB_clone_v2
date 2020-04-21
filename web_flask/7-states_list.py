#!/usr/bin/python3
''' point 7 '''
from models import storage
from models.state import State
from flask import Flask, render_template
app = Flask(__name__)


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
def ses_close():
    '''close session'''
    storage.close()
    	
if __name__ == '__main__':
    app.run(host="0.0.0.0", port="5000")
