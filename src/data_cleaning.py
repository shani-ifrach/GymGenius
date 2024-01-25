import sqlite3
import pandas as pd
import os
from database import print_table
from database import db_connection_wrapper

def csv_to_df(csv_file_path):
    df = pd.read_csv(csv_file_path)
    columns = [i for i in df.head() if r"/" in i]
    main_columns = list({i.split("/")[0]:None for i in df.head() if r"/" in i}.keys())
    for main_column in main_columns:
        values = []
        for value in df[[i for i in columns if i.startswith(main_column)]].values:
            lst = [i for i in value if str(i) != "nan"]
            lst = [i + ", " if not i.endswith('.') and i != lst[-1] else i for i in lst]
            values.append("\n".join(set(lst)))
        df.insert(5, main_column, values)
    df = create_url_info(df)
    return df

@db_connection_wrapper
def df_into_table(conn, df, table_name, if_exists = "append"):
    existing_columns = pd.read_sql(f"PRAGMA table_info({table_name});", conn)['name'].tolist()
    # Filter DataFrame columns based on existing columns in the table
    columns_to_insert = list(filter(lambda col: col in existing_columns, df.columns))

    # Insert data into the SQLite table for existing columns only
    df[columns_to_insert].to_sql(table_name, conn, index=False, if_exists=if_exists)


def create_url_info(df):
    url_column = 'url'
    base_url = r'https://www.google.com/search?q='
    values = []
    for value in df["name"]:
        values.append(base_url + value.replace(" ", "+") + "+exercise")
    df.insert(0, url_column, values)
    return df


if __name__ == '__main__':
    current_dir = os.path.dirname(os.path.abspath(__file__))
    csv_file = os.path.join(os.path.dirname(current_dir), 'data', 'exercises.csv')
    db_file = os.path.join(os.path.dirname(current_dir), 'db', 'sport.db')
    conn = sqlite3.connect(db_file)
    df = csv_to_df(csv_file)
    df_into_table(df, "exercises", if_exists="append")

    conn.close()
