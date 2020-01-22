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


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    """ print number only if its an int """
    return '{} is a number'.format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    """ makes html based on number given template """
    return render_template('5-number.html', number=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def number_odd_even(n):
    """makes html based on even or odd number"""
    return render_template('6-number_odd_or_even.html', number=n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
