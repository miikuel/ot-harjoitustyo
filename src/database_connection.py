import os
import sys
import sqlite3
from dotenv import load_dotenv

load_dotenv()

dirname = os.path.dirname(__file__)
data_dir = os.path.join(dirname, "..", "data")
if not os.path.exists(data_dir):
    os.makedirs(data_dir)

TEST_ENV = os.getenv("TEST_ENV")

if TEST_ENV:
    db_dir = os.getenv("TEST_DB_PATH") or data_dir
    db_file_path = os.path.join(db_dir, "test_database.sqlite")
else:
    db_dir = os.getenv("DB_PATH") or data_dir
    db_file_path = os.path.join(db_dir, "database.sqlite")

if not os.path.exists(db_dir):
    print(f"Ympäristömuuttujassa määriteltyä hakemistoa {db_dir} ei ole olemassa,"
            " luo hakemisto tai poista muuttuja .env tiedostosta"
            " käyttääksesi oletuskonfiguraatiota")
    sys.exit(0)

connection = sqlite3.connect(db_file_path)
connection.row_factory = sqlite3.Row


def get_database_connection():
    return connection
