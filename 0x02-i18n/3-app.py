#!/usr/bin/env python3
"""Module that sets up a Flask-Babel extension"""
from flask import Flask, render_template
from flask_babel import Babel

app = Flask(__name__)
babel = Babel(app)


class Config(object):
    """Configuration class for Flask app"""
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


# Set Babel's values using Config class to the flask app
app.config.from_object('3-app.Config')


@app.route('/', methods=['GET'], strict_slashes=False)
def index() -> str:
    """Default route for flask app"""
    return render_template('3-index.html',
                           title=('home_title'), header=('home_header'))
    # return render_template('3-index.html')


@babel.localeselector
def get_locale() -> str:
    """Determine the best match for the supported languages"""
    return request.accept_languages.best_match(app.config['LANGUAGES'])


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
