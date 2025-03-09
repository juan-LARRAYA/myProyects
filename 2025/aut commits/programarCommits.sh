#!/bin/bash

# Configuración
script_a_ejecutar="./git_auto_push.sh"
cron_temp="/tmp/crontab_temp"
max_ejecuciones=2

# Generar un número aleatorio de ejecuciones (entre 0 y max_ejecuciones)
num_ejecuciones=$((RANDOM % max_ejecuciones))

echo "Generando $num_ejecuciones ejecuciones para hoy..."

# Limpiar las tareas antiguas relacionadas (si las hay)
crontab -l | grep -v "$script_a_ejecutar" > "$cron_temp"

# Crear nuevas tareas en horarios aleatorios
for ((i=1; i<=num_ejecuciones; i++)); do
    hora=$((RANDOM % 24))
    minuto=$((RANDOM % 60))
    echo "$minuto $hora * * * $script_a_ejecutar" >> "$cron_temp"
done

# Actualizar crontab con las nuevas tareas
crontab "$cron_temp"
rm "$cron_temp"

echo "Ejecuciones configuradas en crontab."
