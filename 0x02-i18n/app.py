#!/usr/bin/env python3
"""Simple Flask App module"""
from flask import Flask, render_template, request, g
from flask_babel import Babel, format_datetime
from pytz import timezone
from datetime import datetime


class Config:
    """Config class for Babel"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
babel = Babel(app)
app.config.from_object(Config)

users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_user() -> dict:
    """Get user from request"""
    user_id = request.args.get('login_as')
    if user_id:
        return users.get(int(user_id))
    return None


@app.before_request
def before_request() -> None:
    """Before request handler"""
    user = get_user()
    g.user = user
    g.time = format_datetime(datetime.now())


@babel.localeselector
def get_locale() -> str:
    """Get locale from request"""
    locale = request.args.get('locale')
    if locale and locale in Config.LANGUAGES:
        return locale

    if g.user:
        locale = g.user.get('locale')
        if locale and locale in Config.LANGUAGES:
            return locale

    locale = request.headers.get('locale')
    if locale and locale in Config.LANGUAGES:
        return locale

    return request.accept_languages.best_match(app.config['LANGUAGES'])


@babel.timezoneselector
def get_timezone() -> str:
    """Get timezone from request"""
    zone = request.args.get('timezone')

    if zone:
        try:
            return timezone(zone).zone
        except pytz.exceptions.UnknownTimeZoneError:
            pass

    if g.user:
        try:
            zone = g.user.get('timezone')
            return timezone(zone).zone
        except pytz.exceptions.UnknownTimeZoneError:
            pass

    return app.config['BABEL_DEFAULT_TIMEZONE']


@app.route('/', strict_slashes=False)
def home() -> str:
    """renders a simple html file"""

    return render_template('index.html')


if __name__ == '__main__':
    app.run()
