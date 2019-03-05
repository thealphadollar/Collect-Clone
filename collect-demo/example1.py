import functools

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)

ex1 = Blueprint('example1', __name__, url_prefix='/example1')

@ex1.route('/', methods=('GET', 'POST'))
def example1_root():
    """
    handles the endpoint for example 1
    """

    if request.method == "POST":
        """
        Before upload, raw page
        """
        pass

    elif request.method == "GET":
        """
        to handle upload request
        """
        return render_template("example1_get.html")