#!/usr/bin/python3
from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello():
    """handle request """
    return 'Hello HBNB!'


@app.route('/hbnb')
def hello_hbnb():
    """handle request to path /hbnb """
    return 'HBNB'


@app.route('/c/<text>')
def c_route(text):
    """handle request with a variable """
    return 'C %s' % text.replace('_', ' ')


@app.route('/python/')
@app.route('/python/<text>')
def python(text='is cool'):
    """handle request with a variable and data default """
    return 'Python %s' % text.replace('_', ' ')


@app.route('/number/<int:num>')
def numbers(num):
    """handle request with a variable with specified type """
    return '%d is a number' % num


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
