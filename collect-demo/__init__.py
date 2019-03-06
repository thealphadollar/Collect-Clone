"""
initialization file containing the flask APP class
"""

import os

from flask import Flask, render_template, url_for, request, redirect

from .config import BasicConfig
from .db_handler import DBHandler
from .example1 import ex1
from .example2 import ex2
from .example3 import ex3


def create_app():
    """
    create app and it's methods

    :return: server app
    :rtype: Flask
    """

    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(BasicConfig)
    app.config.from_mapping(
        DATABASE=os.path.join(os.path.expanduser('~'), 'demo.sqlite')
    )
    # context intialized early to setup database and other related services
    app.app_context().push()

    # TODO: uncomment below code for final testing
    # initialize database
    flask_db = DBHandler()

    # adding blueprints
    app.register_blueprint(ex1)
    app.register_blueprint(ex2)
    app.register_blueprint(ex3)

    try:
        os.makedirs(app.instance_path)
    except OSError as err:
        print(err)
        print("Failed to create directory: insufficient permissions or already exist!")

    @app.route('/', methods=["POST", "GET"])
    def root():
        """
        main page to provide and handle all the three examples choices.
        
        :return: main page [GET] or example page [POST]
        :rtype: Flask.template
        """

        if request.method == "GET":
            return render_template('main.html')
        elif request.method == "POST":
            if int(request.form['example_number']) == 1:
                return redirect('/example1')
            elif int(request.form['example_number']) == 2:
                return redirect('/example2')
            else:
                return redirect('/example3')

    return app
