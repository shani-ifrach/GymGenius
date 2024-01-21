from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
import math

def calculate_pi():
    return math.pi # Import the function from the script

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


# Default DAG arguments
default_args = {
    'owner': 'airflow',
    'start_date': datetime(2024, 1, 1),
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

# DAG definition
dag = DAG(
    'my_pipeline',
    default_args=default_args,
    schedule_interval='*/5 * * * *',  # Adjust as needed
)

# Task to execute the Python script
run_python_script = PythonOperator(
    task_id='run_python_script',
    python_callable=calculate_pi,
    dag=dag,
)


task2 = PythonOperator(
    task_id='createfile',
    python_callable=calculate_pi,
    dag=dag,
)

run_python_script >> task2