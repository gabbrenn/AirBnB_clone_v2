#!/usr/bin/python3
"""
starts a Flask web application
"""
from flask import Flask
from markupsafe import escape
app = Flask(__name__)

#route definition
@app.route("/", strict_slashes=False)
def hello_hbnb():
	"""Display Hello HBNB"""
	return "Hello HBNB!"

@app.route("/hbnb", strict_slashes=False)
def hbnb():
	"""Display HBNB"""
	return "HBNB"

@app.route("/c/<text>", strict_slashes=False)
def dynamic_value(text):
	"""Display Dynamic Content"""
	return 'C ' + text.replace('_', ' ')

@app.route("/python/<text>", strict_slashes=False)
def py_values(text = "is cool"):
	"""Display Python is cool"""
	return 'Python ' + text.replace('_', ' ')

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=5000)
