# Eliminación de Páginas Duplicadas en PDF

Este script de Python elimina páginas duplicadas en un archivo PDF utilizando la librería `PyPDF2` y la generación de hashes MD5 para comparar el contenido de las páginas.

## Descripción

El objetivo del script es detectar y eliminar páginas duplicadas en un archivo PDF. Para lograrlo, se extrae el contenido de cada página, se convierte en texto, y se genera un hash MD5 a partir de ese contenido. Si el hash de una página ya ha sido registrado (es decir, si una página es idéntica a otra previamente encontrada), dicha página no se incluye en el archivo PDF de salida.

## Requisitos

- **Python 3.x**
- **PyPDF2**
- **hashlib** (incluido en la biblioteca estándar de Python)

### Instalación de Dependencias

Puedes instalar la librería `PyPDF2` utilizando `pip`:

```bash
pip install PyPDF2
```

## Uso

1. Coloca el archivo PDF que deseas procesar en la misma carpeta donde está el script o proporciona la ruta completa al archivo.
2. Especifica el nombre del archivo PDF de entrada y el nombre del archivo PDF de salida en el código.
3. Ejecuta el script para generar un nuevo archivo PDF sin páginas duplicadas.

### Ejecución

El script está configurado para trabajar con los siguientes archivos:

- **Archivo de entrada:** `Compiladazo.pdf`
- **Archivo de salida:** `Compiladazo_sin_duplicados.pdf`

Para ejecutar el script, simplemente usa:

```bash
python nombre_del_script.py
```

- **Proceso:**
  - Lee todas las páginas del PDF.
  - Genera hashes para cada página.
  - Verifica si el hash ya ha sido visto y, en caso contrario, añade la página al nuevo PDF.

### Variables Importantes:

- **`input_pdf`**: Es el archivo PDF original que contiene potencialmente páginas duplicadas.
- **`output_pdf`**: Es el archivo PDF resultante que se generará sin páginas duplicadas.

## Ejemplo

Si tienes un archivo PDF llamado `Compiladazo.pdf` y quieres eliminar todas las páginas duplicadas, el script guardará un nuevo archivo llamado `Compiladazo_sin_duplicados.pdf` en la misma carpeta con todas las páginas repetidas eliminadas.

