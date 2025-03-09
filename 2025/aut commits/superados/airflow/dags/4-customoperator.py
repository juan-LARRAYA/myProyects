from airflow import DAG
from datetime import datetime
from hellooperator import HelloOperator

with DAG(dag_id="customOperator",
         description="Nuestro primer custom operator",
         start_date=datetime(2022,1,1)) as dag:
    
    t1 = HelloOperator(task_id="hello",
                       name="Freddy")
    

    t1
