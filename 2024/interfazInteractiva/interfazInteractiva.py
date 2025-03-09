import tkinter as tk
from tkinter import ttk
import numpy as np
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Crear la ventana principal
root = tk.Tk()
root.title("Modificación de Ecuación y Gráfico")
root.geometry("600x500")

# Variables de la ecuación
a = tk.DoubleVar(value=1.0)
b = tk.DoubleVar(value=0.0)
c = tk.DoubleVar(value=0.0)

# Configuración de la figura de Matplotlib
fig = Figure(figsize=(5, 4), dpi=100)
ax = fig.add_subplot(111)

# Función para actualizar el gráfico
def actualizar_grafico():
    # Limpiar el gráfico anterior
    ax.clear()
    
    # Generar los datos de la gráfica en función de a, b y c
    x = np.linspace(-10, 10, 100)
    y = a.get() * x**2 + b.get() * x + c.get()
    
    # Dibujar el nuevo gráfico
    ax.plot(x, y, label=f'y = {a.get()}x² + {b.get()}x + {c.get()}')
    ax.legend(loc="upper right")
    
    # Actualizar el canvas
    canvas.draw()

# Canvas de Matplotlib en Tkinter
canvas = FigureCanvasTkAgg(fig, master=root)
canvas.get_tk_widget().pack(pady=20)

# Crear controles para modificar los valores de a, b y c
frame = ttk.Frame(root)
frame.pack(pady=10)

# Función para crear un slider
def crear_slider(variable, etiqueta):
    ttk.Label(frame, text=etiqueta).pack(side="left")
    escala = tk.Scale(frame, from_=-10, to=10, orient="horizontal", resolution=0.1, variable=variable, command=lambda val: actualizar_grafico())
    escala.pack(side="left", padx=5)

# Crear los campos de entrada para a, b y c
def crear_input(variable, etiqueta):
    ttk.Label(frame, text=etiqueta).pack(side="left", padx=5)
    entrada = ttk.Entry(frame, textvariable=variable, width=10)
    entrada.pack(side="left", padx=5)
    
    # Llama a actualizar_grafico cada vez que se modifique el contenido del campo
    entrada.bind("<KeyRelease>", lambda event: actualizar_grafico())

# Sliders para ajustar a, b y c
crear_slider(a, "a:")
crear_slider(b, "b:")
crear_input(c, "c:")


# Llamar a la función de actualización inicial para mostrar el gráfico por primera vez
actualizar_grafico()

# Bucle principal de la GUI
root.mainloop()
