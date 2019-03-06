"""
contains all the methods required for managing example 3
"""
import io

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for, Response
)

from .db_handler import DBHandler

ex3 = Blueprint('example3', __name__, url_prefix='/example3')

@ex3.route('/')
def example3_root():
    return render_template("example3.html")

@ex3.route('/upload', methods=["POST"])
def example3_team_upload():
    f = request.files.get("team_data", None)

    if f is None:
        flash("Invalid file uploaded!")
        return redirect("/example3")

    fileStream = io.StringIO(f.stream.read().decode('utf-8'), newline=None)

    try:
        DBHandler.add_team_data(fileStream)
    except KeyError as _:
        flash("Invalid CSV data!")
        return redirect("/example3")
    
    return render_template("example3_post.html")

@ex3.route('/clear')
def example3_reupload():
    DBHandler.truncate("example3")
    flash("Teams cleared!")
    return redirect("/example3/")