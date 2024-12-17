import os
import sqlite3
from dotenv import load_dotenv

load_dotenv()

dirname = os.path.dirname(__file__)
data_dir = os.path.join(dirname, "..", "data")
if not os.path.exists(data_dir):
    os.makedirs(data_dir)

TEST_ENV = os.getenv("TEST_ENV")

if TEST_ENV:
    TEST_DB_PATH = os.getenv("TEST_DB_PATH") or data_dir
    connection = sqlite3.connect(os.path.join(TEST_DB_PATH, "test_database.sqlite"))
else:
    DB_PATH = os.getenv("DB_PATH") or data_dir
    connection = sqlite3.connect(os.path.join(DB_PATH, "database.sqlite"))
connection.row_factory = sqlite3.Row


def get_database_connection():
    return connection
