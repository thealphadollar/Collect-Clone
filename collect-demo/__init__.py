"""
initialization file containing the flask APP class
"""


import os

from flask import Flask
from flask import render_template

from .config import BasicConfig


def create_app():
    """
    create app and it's methods

    :return: server app
    :rtype: Flask
    """

    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(BasicConfig)
    app.config.from_mapping(
        DATABASE=os.path.join(app.instance_path, 'demo.sqlite')
    )

    try:
        os.makedirs(app.instance_path)
    except OSError as err:
        print(err)
        print("Failed to create directory: insufficient permissions or already exist!")

    @app.route('/')
    def root():
        pass

    return app
