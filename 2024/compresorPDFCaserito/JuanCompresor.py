import fitz  # PyMuPDF
from PIL import Image

def capturar_pantalla_pdf(input_pdf, output_pdf, resolucion=72):
    """
    Captura las páginas de un PDF como imágenes y genera un nuevo PDF a partir de ellas.
    
    - input_pdf: Archivo PDF de entrada.
    - output_pdf: Archivo PDF de salida.
    - resolucion: La resolución de las capturas de pantalla en DPI (por defecto 72).
    """
    # Abrimos el PDF original
    pdf_document = fitz.open(input_pdf)
    
    imagenes = []
    
    for num_pagina in range(pdf_document.page_count):
        # Cargamos la página
        pagina = pdf_document.load_page(num_pagina)
        
        # Capturamos la imagen de la página como pixmap (matriz de píxeles)
        pixmap = pagina.get_pixmap(dpi=resolucion)
        
        # Convertimos el pixmap a imagen PIL
        imagen = Image.frombytes("RGB", [pixmap.width, pixmap.height], pixmap.samples)
        
        # Añadimos la imagen a la lista de imágenes
        imagenes.append(imagen)
    
    # Guardamos las imágenes como un PDF
    if imagenes:
        imagenes[0].save(output_pdf, save_all=True, append_images=imagenes[1:])
    
    pdf_document.close()
    print(f"Nuevo PDF generado como {output_pdf}")

# Uso del código
pdf_entrada = "Animal Farm by George Orwell.pdf"
pdf_salida = "Animal Farm_Compresed.pdf"
capturar_pantalla_pdf(pdf_entrada, pdf_salida, resolucion=150)  # Ajusta la resolución según lo que necesites

