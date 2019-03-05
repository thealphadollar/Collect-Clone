"""
initialization file containing the flask APP class
"""


import os

from flask import Flask
from flask import render_template, url_for

from .config import BasicConfig
from .db_handler import DBHandler
from .example1 import ex1


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

    # TODO: uncomment below code for final testing

    # initialize database
    # flask_db = DBHandler()

    # adding blueprints
    # app.register_blueprint(ex1)

    try:
        os.makedirs(app.instance_path)
    except OSError as err:
        print(err)
        print("Failed to create directory: insufficient permissions or already exist!")

    @app.route('/', methods=["POST", "GET"])
    def root():
        if request.method == "GET":
            return render_template('main.html')
        elif request.method == "POST":
            if request.form['example_number'] == 1:
                return redirect(url_for(example1_root))
            elif request.form['example_number'] == 2:
                return redirect(url_for(example2_root))
            else:
                return redirect(url_for(example3_root))

    return app
