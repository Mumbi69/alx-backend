#!/usr/bin/env python3
"""Parametrize templates"""

from flask import Flask, render_template, request
from flask_babel import Babel


app = Flask(__name__)


babel = Babel(app)


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


SUPPORTED_LOCALES = ["en", "fr", "kg"]


def get_user(user_id):
    """This function gets user information"""
    return users.get(user_id)


@app.before_request
def before_request():
    """Define a function to be executed before all other functions"""
    user_id = request.args.get('login_as')
    if user_id:
        g.user = get_user(int(user_id))
    else:
        g.user = None


class Config:
    """config class with available languages"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)


@babel.localeselector
def get_locale():
    """This function determines the best-matching language"""
    requested_locale = request.args.get('locale')
    if requested_locale and requested_locale in SUPPORTED_LOCALES:
        return requested_locale

    if g.user and g.user['locale'] in SUPPORTED_LOCALES:
        return g.user['locale']

    return request.accept_languages.best_match(app.config['SUPPORTED_LOCALES'])


@app.route('/')
def hello():
    """renders template 6-index.html"""
    return render_template('6-index.html')


if __name__ == '__main__':
    app.run(debug=True)
