#!/usr/bin/env python3
"""Module that sets up a Flask-Babel extension"""

from flask_babel import Babel
from flask import Flask, render_template

app = Flask(__name__)
babel = Babel(app)


class Config:
    """Configuration class for Flask app"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


# Set Babel's values using Config class to the flask app
app.config.from_object(Config)


@app.route('/')
def index():
    """Method rendering index.html template"""
    return render_template('1-index.html')


if __name__ == '__main__':
    app.run(debug=True)
