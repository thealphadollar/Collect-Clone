"""
contains methods to handle database and adjoining operations
"""

import os
import csv
import sqlite3
from contextlib import contextmanager
from datetime import datetime

from flask import current_app, g
from flask.cli import with_appcontext
from julian import to_jd, from_jd

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
        
    @staticmethod
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
    
    @staticmethod
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

    @staticmethod
    def truncate(table_name):
        """
        removes all the rows of the specified table

        :param table_name: name of the table
        :type table_name: string
        """

        with DBHandler.connect() as conn:
            cur = conn.cursor()
            cur.execute("DELETE FROM {};".format(table_name))
            conn.commit()
            cur.execute("VACUUM;")
            conn.commit()
    
    @staticmethod
    def fetch_beyond(date):
        """
        fetches all rows from the table example2 which are beyond the given date
    
        :param date: send entries greater than or equal to this date
        :type date: Datetime.date
        :return: csv formatted string of the relevant database entries
        :rtype: string
        """

        value = to_jd(datetime.strptime(date, "%Y-%m-%d"))
        csv_data = "id,date,data\n"
        try:
            with DBHandler.connect() as conn:
                cur = conn.execute("SELECT * FROM example2 WHERE date >= {}".format(value))
                raw_data = cur.fetchall()
        except sqlite3.Error as err:
            print(err)
        
        for row in raw_data:
            new_row = [i for i in row]
            new_row[1] = from_jd(new_row[1], fmt="jd")
            csv_data = csv_data + ",".join([str(i) for i in new_row]) + "\n"

        return csv_data

    def load_dummy_data(self):
        """
        loads data for example 3 from the dummy data exam2.csv
        """

        with open(EXAMPLE_2_DUMMY_DATA, 'r') as csvFile:
            dr = csv.DictReader(csvFile)
            to_db = [(x['date'], x['data']) for x in dr]
        
        with self.connect() as conn:
            cur = conn.cursor()
            cur.executemany('INSERT INTO example2 (date, data) VALUES (?, ?);', to_db)
            conn.commit()