#!/usr/bin/env python3
"""Basic flask app"""

from flask import Flask, render_template


app = Flask(__main__)


@app.route('/')
def Welcome():
    """represents the function welcome"""
    return render_template('0-index.html')


if __name__ == '__main__':
    app.run(debug=True)
