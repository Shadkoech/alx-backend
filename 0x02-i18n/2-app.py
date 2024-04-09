#!/usr/bin/env python3
"""Module that sets up a Flask-Babel extension"""
from flask_babel import Babel
from flask import Flask, render_template

app = Flask(__name__)
babel = Babel(app)


class Config:
    """Configuration class for Flask app"""
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


# Set Babel's values using Config class to the flask app
app.config.from_object('1-app.Config')


@app.route('/', methods=['GET'], strict_slashes=False)
def index()-> str:
    """Method rendering index.html template"""
    return render_template('1-index.html')


@babel.localeselector
def get_locate() -> str:
    """Determine the best match for the supported languages"""
    return request.accept_languages.best_match(app.config['LANGUAGES'])


if __name__ == '__main__':
    app.run(port="5000", host="0.0.0.0")
