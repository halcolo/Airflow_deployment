from datetime import timedelta, datetime
from airflow import DAG
from AirFLow import Variable
# from airflow.models import Variable
from airflow.operators.python_operator import PythonOperator
from clean_data import clean_load

default_args = {
    # Set variables at the AirFLow variables page
    # and import Airflow.Variable.
    "owner": Variable.get("dag_owner"),
    "depends_on_past": False,
    "start_date": datetime(2018, 5, 20),
    "email": Variable.get("dag_email"),
    # If you have various email adress replace with follow code.
    # At the variables you copy mails as mail1@mail.com,mail2@mail.com
    # [mail.strip() for mail in Variable.get('dag_emails_report').split(',')]
    "email_on_failure": Variable.get("dag_email_failure"),
    "email_on_retry": Variable.get("dag_email_retry"),
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
