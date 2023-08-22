from airflow import DAG
from datetime import datetime


with DAG('user_processing', start_date = datetime(2023, 8, 23),
         schedule_interval = '@daily', catchup = False) as dag:
    None
    
         
        