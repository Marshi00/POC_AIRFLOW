"""
testing tasks 
docker-compose ps
docker exec -it poc_airflow-airflow-scheduler-1 /bin/bash

""" 

"""
run a docker file 
docker-compose up -d
"""

"""
copy the cfg file from docker to your local
docker cp poc_airflow-airflow-scheduler-1:/opt/airflow/airflow.cfg .
"""

"""
run flower
docker-compose down && docker-compose --profile flower up -d
"""