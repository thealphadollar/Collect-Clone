"""
contains methods to handle database and adjoining operations
"""

import sqlite3

from flask import current_app, g
from flask.cli import with_appcontext


class DBHandler:
    """
    class encapsulating all database methods    
    """
    
    def __init__(self):
        conn = self.connect()

        with current_app.open_resource('init.sql') as f:
            conn.executescript(f.read().decode('utf-8'))

        self.load_dummy_data()

    def connect():
        if 'db' not in g:
            g.db = sqlite3.connect(
                current_app.config['DATABASE'],
                detect_types=sqlite3.PARSE_DECLTYPES
            )
            g.db.row_factory = sqlite3.Row
        
        return g.db

    def close_conn():
        db = g.pop('db', None)

        if db is not None:
            db.close()
    
    def load_dummy_data(self):
        # TODO: Create and Load Dummy Data here