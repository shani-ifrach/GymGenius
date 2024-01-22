from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime, timedelta
import sys
sys.path.append(r"C:\Users\LIRAZ\PycharmProjects\GymGenius\hdfs")
from hdfs.hdfs_funcs import create_csv_file

default_args = {
    'owner': 'your_name',
    'start_date': datetime(2022, 1, 1),
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

dag = DAG(
    'my_simple_dag',
    default_args=default_args,
    description='A simple example DAG',
    schedule_interval=timedelta(minutes=2),  # Set the frequency of DAG runs
)

task_1 = PythonOperator(
    task_id='task1',
    python_callable=create_csv_file,
    dag=dag,
)

task_1