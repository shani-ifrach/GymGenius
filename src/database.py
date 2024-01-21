import sqlite3
import os
import pandas as pd
import sqlite3

def db_connection_wrapper(func):
    def wrapper(*args, **kwargs):
        current_dir = os.path.dirname(os.path.abspath(__file__))
        db_path = os.path.join(os.path.dirname(current_dir), 'db', 'sport.db')
        connection = sqlite3.connect(db_path)
        result = func(connection, *args, **kwargs)
        connection.close()

        return result

    return wrapper

def create_database(db_file):
    connection = sqlite3.connect(db_file)
    cursor = connection.cursor()
    connection.commit()
    connection.close()

@db_connection_wrapper
def print_table(connection, table_name):
    cursor = connection.cursor()
    cursor.execute(f'SELECT * FROM {table_name}')
    rows = cursor.fetchall()
    print("Column names:", [description[0] for description in cursor.description])
    for row in rows:
        print(row)

@db_connection_wrapper
def create_table(connection, table_name):
    cursor = connection.cursor()
    create_table_query = f'''
        CREATE TABLE IF NOT EXISTS {table_name} (
            id INTEGER PRIMARY KEY,
            bodyPart TEXT,
            equipment TEXT,
            name TEXT,
            target TEXT,
            secondaryMuscles TEXT,
            instructions TEXT,
            url TEXT,
            clicks_num INTEGER DEFAULT 0,
            likes_num INTEGER DEFAULT 0,
            done_num INTEGER DEFAULT 0
        )
    '''

    # Execute the SQL query to create the table
    cursor.execute(create_table_query)

    # Commit the changes and close the connection
    connection.commit()


@db_connection_wrapper
def show_tables(connection):
    print(connection)
    cursor = connection.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cursor.fetchall()

    print("Tables in the database:")
    for table in tables:
        print(table[0])

@db_connection_wrapper
def get_db_as_df(connection, table_name):
    return pd.read_sql(f"SELECT * FROM {table_name};", connection)

@db_connection_wrapper
def delete_table(conn, table_name):
    cursor = conn.cursor()
    cursor.execute(f'DROP TABLE IF EXISTS {table_name}')
    conn.commit()
    cursor.close()


if __name__ == "__main__":
    current_dir = os.path.dirname(os.path.abspath(__file__))
    db_file = os.path.join(os.path.dirname(current_dir), 'db', 'sport.db')
    #connection = sqlite3.connect(db_file)
    #show_tables(connection)
    table_name = 'exercises7'
    #create_table(connection, table_name)
    #delete_table(connection, table_name)
    print_table(table_name)
    #show_tables(connection)
    #connection.close()