#!/usr/bin/env python3
""" basic flask app """
from flask import Flask, render_template
from flask_babel import Babel


class Config:
    """ configuration class to start """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
""" babel init """
babel = Babel(app)


@app.route('/')
def index():
    """ main method """
    return render_template('1-index.html')


@babel.localeselector
def get_locale():
    """ function with the babel.localeselector
    decorator. Use request.accept_languages """
    return request.accept_languages.best_match(app.config['LANGUAGE'])


if __name__ == '__main__':
    app.run(debug=True)
