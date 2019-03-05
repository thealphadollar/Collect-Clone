import io

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)

from .db_handler import DBHandler

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
        f = request.files['csv_file']
        fileStream = io.StringIO(f.stream.read().decode('utf-8'), newline=None)

        try:
            DataHandler.add_exam1_data(fileStream)
        except Exception as err:
            print(err)
            return redirect(url_for(example1_root))
        
        return render_template("example1_post.html")

    elif request.method == "GET":
        """
        to handle upload request
        """
        return render_template("example1_get.html")

@ex1.route('/clear')
def clear_db:
    """
    clears the example 1 database
    """
    DBHandler.trucate('example1')
    flash("example1 table cleared!")
    return redirect(url_for(example1_root))