#!/usr/bin/env python3
"""Basic flask app"""

from flask import Flask, render_template
from flask_babel import Babel


app = Flask(__name__)


babel = Babel(app)


class Config:
    """config class with available languages"""
    LANGUAGES = ["en", "fr"]


app.config.from_object(Config)


@app.route('/')
def index():
    """renders template 1-index.html"""
    return render_template('1-index.html')


if __name__ == '__main__':
    app.run(debug=True)
