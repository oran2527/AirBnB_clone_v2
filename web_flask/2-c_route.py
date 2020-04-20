#!/usr/bin/python3
''' point 2 '''

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
    '''route hbnb function'''
    var = text.replace("_", " ")
    return 'C ' + var

if __name__ == '__main__':
    app.run(host="0.0.0.0", port="5000")
