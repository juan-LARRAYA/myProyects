import PyPDF2
import hashlib

def get_page_hash(page):
    """Genera un hash del contenido de una página."""
    page_text = page.extract_text()
    return hashlib.md5(page_text.encode('utf-8')).hexdigest()

def remove_duplicate_pages(input_pdf, output_pdf):
    """Elimina todas las páginas duplicadas de un archivo PDF utilizando hashing."""
    with open(input_pdf, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        writer = PyPDF2.PdfWriter()

        seen_hashes = set()

        for i in range(len(reader.pages)):
            current_page = reader.pages[i]
            page_hash = get_page_hash(current_page)
            
            # Solo agrega la página si su hash no ha sido visto antes
            if page_hash not in seen_hashes:
                writer.add_page(current_page)
                seen_hashes.add(page_hash)

        # Guardar el nuevo archivo PDF sin duplicados
        with open(output_pdf, 'wb') as output_file:
            writer.write(output_file)

# Especifica el archivo de entrada y el archivo de salida
input_pdf = 'Compiladazo.pdf'
output_pdf = 'Compiladazo_sin_duplicados.pdf'

# Ejecuta la función para eliminar páginas duplicadas
remove_duplicate_pages(input_pdf, output_pdf)

print(f"Archivo guardado como {output_pdf} sin páginas duplicadas.")
