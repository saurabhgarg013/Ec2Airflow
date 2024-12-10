from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta

def print_hello():
    print("Hello from Airflow!")

# Define default_args
default_args = {
    'owner': 'airflow',
    'retries': 1,
    'retry_delay': timedelta(minutes=5),  # You can define retry delay here
    'start_date': datetime(2024, 12, 9),
}

#A single task (hello_task) within the DAG.
# Define the DAG
with DAG(
    'example_dag',
    default_args=default_args,
    description='An example DAG',
    schedule_interval=None,  # Set to None to trigger manually
    catchup=False,
) as dag:
    # Define the Python task
    hello_task = PythonOperator(
        task_id='hello_task',
        python_callable=print_hello,
    )
