#!/usr/bin/env python3

from datetime import datetime, timedelta

from airflow.models import DAG

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
    pass