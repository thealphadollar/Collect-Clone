import functools

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)

ex1 = Blueprint('example1', __name__, url_prefix='/example1')

