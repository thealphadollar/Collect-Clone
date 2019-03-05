"""
contains methods to handle database and adjoining operations
"""

import os
import sqlite3
from contextlib import contextmanager

from flask import current_app, g
from flask.cli import with_appcontext

EXAMPLE_2_DUMMY_DATA = os.path.join(os.path.dirname(os.path.relpath(__file__)),
                                    'dummy-input', 'exam2.csv')


class DBHandler:
    """
    class encapsulating all database methods    
    """
    
    def __init__(self):
        """
        initializes database system and load dummy data for example 3
        """

        with self.connect() as conn:
            with current_app.open_resource('init.sql') as f:
                conn.executescript(f.read().decode('utf-8'))

        self.load_dummy_data()
        

    @contextmanager
    def connect():
        """
        context manager that yields a connection to the database and closes
        it as soon as the context ends
        """

        if 'db' not in g:
            g.db = sqlite3.connect(
                current_app.config['DATABASE'],
                detect_types=sqlite3.PARSE_DECLTYPES
            )
            g.db.row_factory = sqlite3.Row
        
        yield g.db
        
        db = g.pop('db', None)

        if db is not None:
            db.close()
    
    def add_exam1_data(csvStream):
        """
        adds data uploaded via csv for example1 to the table
        
        :param csvStream: uploaded csv file
        :type csvStream: FileStream
        """

        dr = csv.DictReader(csvStream)
        to_db = [(x['data1'], x['data2'], x['data3']) for x in dr]

        with DBHandler.connect() as conn:
            cur = conn.cursor()
            cur.executemany('INSERT INTO example1 (data1, data2, data3) VALUES (?, ?, ?);', to_db)
            conn.commit()

    def truncate(table_name):
        """
        removes all the rows of the specified table

        :param table_name: name of the table
        :type table_name: string
        """

        with DBHandler.connect() as conn:
            cur = conn.cursor()
            cur.execute("TRUNCATE TABLE {}".format(table_name))
            conn.commit()

    def load_dummy_data(self):
        """
        loads data for example 3 from the dummy data exam2.csv
        """

        with open(EXAMPLE_2_DUMMY_DATA, 'rb') as csvFile:
            dr = csv.DictReader(csvfile)
            to_db = [(x['date'], x['data']) for x in dr]
        
        with self.connect() as conn:
            cur = conn.cursor()
            cur.executemany('INSERT INTO example2 (date, data) VALUES (?, ?);', to_db)
            conn.commit()