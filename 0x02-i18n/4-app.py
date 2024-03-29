#!/usr/bin/env python3
"""Parametrize templates"""

from flask import Flask, render_template, request
from flask_babel import Babel


app = Flask(__name__)


babel = Babel(app)


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
    if requested_locale in config.LANGUAGES:
        return requested_locale
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def hello():
    """renders template 4-index.html"""
    return render_template('4-index.html')


if __name__ == '__main__':
    app.run(debug=True)
