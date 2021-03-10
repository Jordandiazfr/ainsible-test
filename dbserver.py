import psycopg2
from psycopg2 import Error
import os
from dotenv import load_dotenv
from dotenv import dotenv_values
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)


class PostGreSQL:
    def __init__(self):
        self.host = os.environ.get('HOST')
        self.db_name = os.environ.get('DBNAME')
        self.user = os.environ.get('USER')
        self.password = os.environ.get('PASS')
        self.sslmode = "require"
        self.port = os.environ.get('PORT')

    def connect(self):
        # Construct connection string
        try:
            # Connect to an existing database
            connection = psycopg2.connect(user=self.user, password=self.password,
                                          host=self.host, port=self.port, database=self.db_name, sslmode=self.sslmode)

            # Create a cursor to perform database operations
            cursor = connection.cursor()

            # Print PostgreSQL details
            print("Connected to the database")
            return connection
        except (Exception, Error) as error:
            print("Error while connecting to PostgreSQL", error)

    def create_table(self, table_name: str):
        conn = self.connect()
        cursor = conn.cursor()
        SQL_QUERY = """CREATE TABLE IF NOT EXISTS {0} (
            id_cours SERIAL PRIMARY KEY,
            title VARCHAR(250) UNIQUE) ;""".format(table_name)
        cursor.execute(SQL_QUERY)
        conn.commit()
        cursor.close()
        conn.close()
        print("Table " + table_name + " created")

    def select(self, table):
        conn = self.connect()
        cursor = conn.cursor()
        # Fetch all rows from table
        cursor.execute(f"SELECT * FROM {table}")
        rows = cursor.fetchall()
        # Print all rows
        cursor.close()
        conn.close()
        return rows

    def insert(self, table, data: list):
        conn = self.connect()
        c = conn.cursor()
        if data != "":
            query = """INSERT INTO %s (title) VALUES (%s);""" % (
                table, data)
            #new_data = data
            c.execute(query)
            conn.commit()
            c.close()
            conn.close()

    def drop(self):
        pass

    def exec(self, query):
        conn = self.connect()
        c = conn.cursor(dictionary=True)
        c.execute(query)
        # Store + print the fetched data
        result = c.fetchall()
        # Remember to save + close
        conn.commit()
        c.close()
        conn.close()

        return result
