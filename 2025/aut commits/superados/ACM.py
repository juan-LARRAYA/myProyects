import os
import random
from datetime import datetime, timedelta
import subprocess

# Configuración
project_path = os.path.dirname(os.path.abspath(__file__))  # Ruta del script actual
repo_url = "git@github.com:juan-LARRAYA/busqueda.git"  # URL de tu repositorio
branch_name = "main"  # Cambia según la rama principal de tu repositorio
min_commits = 1
max_commits = 4
date_file = "fecha_actual.txt"  # Nombre del archivo a actualizar

# Función para generar un mensaje de commit
def generate_commit_message():
    return f"Commit automático: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"

# Actualizar el archivo con la fecha de hoy
def update_date_file():
    today = datetime.now().strftime("%Y-%m-%d")
    file_path = os.path.join(project_path, date_file)
    with open(file_path, "w") as file:
        file.write(f"Fecha actual: {today}\n")
    print(f"Archivo actualizado: {file_path} con la fecha {today}")

# Generar una lista de fechas y horas aleatorias para los commits de la semana
def generate_random_commit_times(num_commits):
    start_time = datetime.now().replace(hour=0, minute=0, second=0, microsecond=0)
    end_time = start_time + timedelta(days=7)  # Siguiente semana
    return sorted(
        start_time + timedelta(seconds=random.randint(0, int((end_time - start_time).total_seconds())))
        for _ in range(num_commits)
    )

# Ejecutar un comando en la terminal
def run_command(command):
    subprocess.run(command, shell=True, check=True)

# Automatizar commits
def automate_commits():
    # Cambiar al directorio del proyecto
    os.chdir(project_path)
    
    # Actualizar el archivo de fecha
    update_date_file()
    
    # Inicializar el repositorio si no está configurado
    try:
        run_command("git rev-parse --is-inside-work-tree")
    except subprocess.CalledProcessError:
        print("Inicializando repositorio local...")
        run_command("git init")
        run_command(f"git remote add origin {repo_url}")
        run_command(f"git checkout -b {branch_name}")

    # Número aleatorio de commits entre min_commits y max_commits
    num_commits = random.randint(min_commits, max_commits)
    commit_times = generate_random_commit_times(num_commits)
    
    for commit_time in commit_times:
        # Cambiar la fecha del sistema para el commit
        os.environ["GIT_AUTHOR_DATE"] = commit_time.strftime("%Y-%m-%dT%H:%M:%S")
        os.environ["GIT_COMMITTER_DATE"] = commit_time.strftime("%Y-%m-%dT%H:%M:%S")
        
        # Crear y realizar el commit
        run_command("git add .")
        run_command(f'git commit -m "{generate_commit_message()}"')
        print(f"Commit realizado en: {commit_time}")
    
    # Empujar los cambios al repositorio remoto
    print("Subiendo los commits al repositorio remoto...")
    run_command(f"git push -u origin {branch_name}")

# Ejecutar el script
if __name__ == "__main__":
    automate_commits()
