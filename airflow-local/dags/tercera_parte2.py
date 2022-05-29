#!/usr/bin/env python3

from datetime import datetime, timedelta

from airflow.models import DAG
from airflow.operators.dummy_operator import DummyOperator
from operators.my_operators import TimeDiff

default_args = {
'owner': 'airflow',
'depends_on_past': False,
'start_date': datetime(1900, 1, 1),
'retries': 1,
'retry_delay': timedelta(seconds=5)
}

with DAG(
    'test_time',
    default_args=default_args,
    description='DAG Test time diff',
    schedule_interval='0 3 * * *',
    start_date=datetime.today()
) as dag:
    start = DummyOperator(task_id='start', dag=dag)
    end = DummyOperator(task_id='end', dag=dag)
    operator_task = TimeDiff(diff_date=datetime(1987, 7, 1, 17, 0, 0), task_id='time_diff_task', dag=dag)
    
start >> operator_task >> end

# 5
# Un Hook es una interfaz de alto nivel que permite establecer una conexión con una API o base de datos externa. Se integran con las Conexiones para poder obtener las credenciales.
# Las conexiones son el conjunto de parámetros que permite establecer la conexión con un sistema externo. Se crean desde el frontal web y se almacena la información cifrada.