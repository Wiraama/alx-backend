#!/usr/bin/env python3
'''Task 6: Force locale with URL parameter
'''

from flask import Flask, render_template, request, g
from flask_babel import Babel


class Config:
    '''Config class'''

    DEBUG = True
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
app.url_map.strict_slashes = False
babel = Babel(app)

users = {
        1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
        2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
        3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
        4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"}
        }


def get_user():
    """ get user from db """
    user_id = request.args.get("login_as")

    # convertes to digit if string
    if user_id and user_id.isdigit():
        user_id = int(user_id)

    # lets see is user exist
    if user_id in users:
        user = users[user_id]
        return {
                "id": user_id,
                "name": user["name"],
                "locale": user["locale"],
                "timezone": user["timezone"]
                }
    return None


@app.before_request
def before_request():
    """ find user if any set as global flask.g.user """
    g.user = get_user()


@babel.localeselector
def get_locale() -> str:
    """Retrieves the locale for a web page.

    Returns:
        str: best match
    """
    locale = request.args.get('locale')
    if locale in app.config['LANGUAGES']:
        return locale

    if g.get('user') and g.user.get("locale") in app.config['LANGUAGES']:
        return g.user['locale']
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def index() -> str:
    '''default route

    Returns:
        html: homepage
    '''
    return render_template("5-index.html")


if __name__ == "__main__":
    app.run()
