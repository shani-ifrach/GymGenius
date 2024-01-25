import sqlite3
import os
import data_cleaning
import database
from utils.read_files import project_directory
from utils.read_files import yaml_data


def main():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    db_file = os.path.join(project_directory, 'data', 'db', 'sport.db')
    database.create_database(db_file)
    create_table_query_exercises = yaml_data['exercises_desc']
    database.create_table(create_table_query_exercises)
    csv_file = os.path.join(os.path.dirname(current_dir), 'data', 'exercises.csv')
    df = data_cleaning.csv_to_df(csv_file)
    data_cleaning.df_into_table(df, yaml_data['exercises_table_name'], if_exists="append")
    print(database.print_table(yaml_data['exercises_table_name']))




if __name__ == '__main__':
    main()