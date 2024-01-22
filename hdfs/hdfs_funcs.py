from datetime import datetime
import os
import pandas as pd
from src.database import get_db_as_df

script_directory = os.path.dirname(os.path.abspath(__file__))


def create_csv_file():
    file_path = os.path.join(script_directory, "events_data", str(datetime.now().date()) + ".csv")
    df = pd.DataFrame()
    column_names = {"id": int, "time": str}
    for column, dtype in column_names.items():
        df[column] = pd.Series(dtype=dtype)
    df.to_csv(file_path, index=False)


def update_csv_file(id):
    csv_file = os.path.join(script_directory, "events_data", str(datetime.now().date()) + ".csv")
    new_data = {'id': [id], "time": [str(datetime.now())]}
    new_df = pd.DataFrame(new_data)
    new_df.to_csv(csv_file, sep=',', mode='a', header=False, index=False)


if __name__ == '__main__':
    create_csv_file()
    update_csv_file(0)
    table_df = get_db_as_df('exercises')
    condition = table_df['name'] == "run"
    update_csv_file(table_df.loc[condition, 'id'].values[0])