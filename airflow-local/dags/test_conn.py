#!/usr/bin/env python3

from datetime import datetime, timedelta

from airflow.models import DAG
from airflow.operators.dummy_operator import DummyOperator
from airflow.operators.http_operator import SimpleHttpOperator
import json

default_args = {
'owner': 'airflow',
'depends_on_past': False,
'start_date': datetime(1900, 1, 1),
'retries': 1,
'retry_delay': timedelta(seconds=5)
}

with DAG(
    'test_conn',
    default_args=default_args,
    description='DAG Test Connection',
    schedule_interval='0 3 * * *',
    start_date=datetime.today()
) as dag:
    start = DummyOperator(task_id='start', dag=dag)
    end = DummyOperator(task_id='end', dag=dag)
    task_get_posts = SimpleHttpOperator(
        task_id='get_posts',
        http_conn_id='api_posts',
        endpoint='posts/',
        method='GET',
        response_filter=lambda response: json.loads(response.text),
        log_response=True
    )

start >> task_get_posts >> end