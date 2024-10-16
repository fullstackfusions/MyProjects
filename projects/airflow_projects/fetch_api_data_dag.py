from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime, timedelta
from my_module import run_all_apis_in_parallel  # Replace with your actual import

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2024, 10, 1),
    'retries': 3,
    'retry_delay': timedelta(minutes=5),
}

dag = DAG(
    'api_data_fetch_dag',
    default_args=default_args,
    description='DAG to fetch paginated API data and store in S3',
    schedule_interval=timedelta(days=1),
)

def fetch_api_data():
    s3_bucket_name = 'your-s3-bucket-name'
    run_all_apis_in_parallel(s3_bucket_name)

# Create a task to run the API fetch process
fetch_api_task = PythonOperator(
    task_id='fetch_api_data_task',
    python_callable=fetch_api_data,
    dag=dag,
)

fetch_api_task
