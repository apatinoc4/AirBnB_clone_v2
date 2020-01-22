#!/usr/bin/python3
""" starts a flask web app """
from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """ display message when url is triggered """
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """ print HBNB when in new route """
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c(text):
    """ prints C + users input """
    msg = 'C {}'.format(text)
    msg = msg.replace('_', ' ')
    return msg


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python(text='is_cool'):
    """ inputs for python and python/text routes """
    msg = 'Python {}'.format(text)
    msg = msg.replace('_', ' ')
    return msg


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
