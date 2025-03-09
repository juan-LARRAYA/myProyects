from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator
from datetime import datetime

def myFunction():
    #raise Exception
    pass

with DAG(dag_id="6.1-monitoreando",
         description="Probando el monitoreo",
         schedule_interval="@daily",
         start_date=datetime(2022, 5, 1),
         end_date=datetime(2023, 6, 1)) as dag:

    t1 = BashOperator(task_id="tarea1",
                      bash_command="sleep 2 && echo 'Tarea 1'")

    t2 = BashOperator(task_id="tarea2",
                      bash_command="sleep 2 && echo 'Tarea 2'")

    t3 = BashOperator(task_id="tarea3",
                      bash_command="sleep 2 && echo 'Tarea 3'")

    t4 = BashOperator(task_id="tarea4",
                      bash_command="sleep 2 && echo 'Tarea 4'")
    t5 = PythonOperator(task_id="tarea5",
                        python_callable=myFunction)

    t1 >> t2 >> t3 >> t4 >> t5

    