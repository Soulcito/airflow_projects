from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.bash import BashOperator

default_args = {
  'owner': 'sould',
  'retries': 5,
  'retry_delay': timedelta(minutes=5)
}

with DAG(
    dag_id='dag_with_catchaup_backfill_v02',
    default_args= default_args,
    start_date=datetime(2023,7,1),
    schedule_interval='@daily',
    catchup=False
  ) as dag:
  task1 = BashOperator(
    task_id = 'task1' ,
    bash_command='echo This is a simple bash command!'
  )