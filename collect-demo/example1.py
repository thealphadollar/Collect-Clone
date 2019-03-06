"""
contains all the methods required for managing example 1
"""


import io

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)

from .db_handler import DBHandler

ex1 = Blueprint('example1', __name__, url_prefix='/example1')

@ex1.route('/')
def example1_root():
    """
    handles the endpoint for example 1 uploading processing
    """
    return render_template("example1_get.html")

@ex1.route('/upload', methods=["POST"])
def upload():
    """
    endpoint to handle upload of the csv file
    """

    f = request.files.get('csv_data', None)

    if f is None:
        flash("Invalid file uploaded!")
        return redirect("/example1")

    fileStream = io.StringIO(f.stream.read().decode('utf-8'), newline=None)

    try:
        DBHandler.add_exam1_data(fileStream)
    except KeyError as _:
        flash("Invalid CSV data!")
        return redirect("/example1")
    
    return render_template("example1_post.html")    


@ex1.route('/clear')
def clear_db():
    """
    clears the example 1 database
    """
    DBHandler.truncate('example1')
    flash("example1 table cleared!")
    return redirect("/example1")