#!/usr/bin/env python3
"""Simple Flask App module"""
from flask import Flask, render_template
from flask_babel import Babel


class Config:
    """Config class for Babel"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
babel = Babel(app)
app.config.from_object(Config)


@app.route('/', strict_slashes=False)
def home() -> str:
    """renders a simple html file"""
    return render_template('1-index.html')


if __name__ == '__main__':
    app.run()
