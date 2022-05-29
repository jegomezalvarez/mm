#!/usr/bin/env python3

from datetime import datetime, timedelta

from airflow.models import DAG
from airflow.operators.dummy_operator import DummyOperator

default_args = {
'owner': 'airflow',
'depends_on_past': False,
'start_date': datetime(1900, 1, 1),
'retries': 1,
'retry_delay': timedelta(seconds=5)
}

# 1
with DAG(
    'test',
    default_args=default_args,
    description='DAG Airflow',
    schedule_interval='0 3 * * *',
    start_date=datetime.today()
) as dag:
    start = DummyOperator(task_id='start', dag=dag)
    end = DummyOperator(task_id='end', dag=dag)
    task_1 = DummyOperator(task_id='task_1', dag=dag)
    task_2 = DummyOperator(task_id='task_2', dag=dag)
    task_3 = DummyOperator(task_id='task_3', dag=dag)
    task_4 = DummyOperator(task_id='task_4', dag=dag)
    task_5 = DummyOperator(task_id='task_5', dag=dag)
    task_6 = DummyOperator(task_id='task_6', dag=dag)

# 2
# start >> end

# 3
start >> [task_1,task_3,task_5] >> task_2 >> end
start >> [task_1,task_3,task_5] >> task_4 >> end
start >> [task_1,task_3,task_5] >> task_6 >> end