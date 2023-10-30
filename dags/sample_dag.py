from airflow import DAG, Dataset
from airflow.operators.bash import BashOperator
from datetime import datetime

with DAG(
 dag_id="my_dag",
 start_date=datetime(2016, 1, 1),
 schedule="@daily",
 default_args={"retries": 2},
):
    op = BashOperator(task_id="hello_world", bash_command="Hello World!")
    print(op.retries)
