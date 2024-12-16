import os
import sqlite3

dirname = os.path.dirname(__file__)
data_dir = os.path.join(dirname, "..", "data")
if not os.path.exists(data_dir):
    os.makedirs(data_dir)

connection = sqlite3.connect(os.path.join(data_dir, "database.sqlite"))
connection.row_factory = sqlite3.Row


def get_database_connection():
    return connection
