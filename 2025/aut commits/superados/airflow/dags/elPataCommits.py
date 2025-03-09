from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.bash import BashOperator

with DAG(
    dag_id='commiteando_cosas',
    description='Crea un archivo de texto con la fecha del día y lo sube al repositorio',
    schedule_interval='* * * * *',  # Ejecutar cada minuto
    start_date=datetime(2024, 12, 20),  # Cambia esta fecha según tu necesidad
    catchup=False,  # Evitar ejecución retroactiva
    tags=['ejemplo']
) as dag:
    
    check = BashOperator(
        task_id='check',
        bash_command="""
        echo && 
        whoami && 
        echo && 
        pwd && 
        echo
        """
    )

    # Operador Bash para crear el archivo de texto
    create_file_task = BashOperator(
        task_id='crear_archivo_fecha_task',
        bash_command="""
        today_date=$(date '+%Y-%m_%H-%M-%S')
        echo "Archivo creado el $today_date" > juan.txt
        """
    )

    # Operador Bash para hacer commit y push al repositorio
    commit_and_push_task = BashOperator(
        task_id='commit_and_push_task',
        bash_command="""
        git add . &&
        git commit -m "Commit diario: $(date '+%Y-%m')" &&
        git push origin main
        """
    )

# Definimos la secuencia de las tareas
check >> create_file_task >> commit_and_push_task
