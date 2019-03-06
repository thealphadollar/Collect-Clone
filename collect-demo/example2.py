"""
contains all the methods required for managing example 1
"""

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for, Response
)

from .db_handler import DBHandler

ex2 = Blueprint('example2', __name__, url_prefix='/example2')

@ex2.route('/')
def example2_root():
    """
    serve example2 template to allow users to make query
    for exporting data
    """
    return render_template("example2.html")

@ex2.route('/fetch', methods=["POST"])
def example2_req():
    """
    returns csv data with values beyond the particular date
    """
    date = request.form.get('date', None)
    if date is None:
        flask("No date entered!")
        return render_template("example2.html")

    csv_data = DBHandler.fetch_beyond(date)
    return Response(
        csv_data,
        mimetype="text/csv",
        headers={"Content-disposition":"attachment; filename=DataExport.csv"}
    )