import sqlite3
import os
import data_cleaning
import database

def main():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    db_file = os.path.join(os.path.dirname(current_dir), 'db', 'sport.db')
    database.create_database(db_file)
    table_name = 'exercises'
    database.create_table(table_name)
    csv_file = os.path.join(os.path.dirname(current_dir), 'data', 'exercises.csv')
    df = data_cleaning.csv_to_df(csv_file)
    data_cleaning.df_into_table(df, table_name, if_exists="append")


if __name__ == '__main__':
    main()