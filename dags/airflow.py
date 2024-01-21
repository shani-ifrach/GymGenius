from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python_operator import PythonOperator

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2022, 1, 1),
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

dag = DAG(
    'my_dag',
    default_args=default_args,
    description='A simple DAG',
    schedule_interval=timedelta(days=1),
)

def create_text_file():
    """
    Create a text file with the given file path and content.

    Parameters:
    - file_path (str): The path to the text file.
    - content (str): The content to be written to the file.

    Returns:
    - bool: True if the file creation is successful, False otherwise.
    """
    file_path = r"C:\Users\LIRAZ\PycharmProjects\sport\airflow" + "\\" + datetime.now() + ".txt"
    content = "helloooooo" + datetime.now()
    try:
        with open(file_path, 'w') as file:
            file.write(content)
        print(f"File '{file_path}' created successfully.")
        return True
    except Exception as e:
        print(f"Error creating file '{file_path}': {str(e)}")
        return False

def json():
    file_path = r"C:\Users\LIRAZ\PycharmProjects\sport\airflow" + "\\" + datetime.now() + ".json"

    with open(file_path, 'w') as file:
        file.write({"n":324})

task1 = PythonOperator(
    task_id='create_text_file',
    python_callable=create_text_file,
    dag=dag,
)

task2 = PythonOperator(
    task_id='json',
    python_callable=json,
    dag=dag,
)

task1 >> task2
