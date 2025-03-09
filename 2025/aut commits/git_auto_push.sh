#!/bin/bash

# Obtener la fecha y hora actual en formato "YYYY-MM-DD HH:MM:SS"
fecha_hoy=$(date +"%Y-%m-%d %H:%M:%S")

# Crear un archivo de texto con la fecha y hora como contenido
archivo="fecha_actual.txt"
echo "Fecha y hora: $fecha_hoy" > "$archivo"
echo "Archivo $archivo creado con la fecha y hora actuales."

# Agregar los cambios al staging de Git
git add .

# Crear un commit con la fecha de hoy como mensaje
git commit -m "Actualización: $fecha_hoy"
echo "Commit realizado con el mensaje: 'Actualización: $fecha_hoy'"

# Hacer push al repositorio remoto
git push
echo "Cambios enviados al repositorio remoto."

# Finalización del script
echo "Script finalizado."
