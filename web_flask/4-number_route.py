#!/usr/bin/python3
''' point 4 '''

from flask import Flask
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


if __name__ == '__main__':
    app.run(host="0.0.0.0", port="5000")
