from datetime import timedelta, datetime
from airflow import DAG
# from airflow.models import Variable
from airflow.operators.python_operator import PythonOperator
from clean_data import clean_load

default_args = {
    "owner": "<YOUR NAME>",
    "depends_on_past": False,
    "start_date": datetime(2018, 5, 20),
    "email": ["<your@mail.com>"],
    "email_on_failure": False,
    "email_on_retry": False,
    "retries": 0,
    "retry_delay": timedelta(minutes=5),
}

dag = DAG("airflow-jalfons",
          default_args=default_args,
          schedule_interval='@daily',
          catchup=False
          )

t1 = PythonOperator(
    task_id='pipeline_test',
    provide_context=True,
    python_callable=clean_load,
    dag=dag)
