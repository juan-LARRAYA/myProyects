import cv2
import matplotlib.pyplot as plt
from IPython.display import Image
import numpy as np
import random

# Crear una imagen en blanco
height, width = 400, 800
img = np.ones((height, width, 3), np.uint8) * 255

# Escribir el mensaje oculto en azul
mensaje = "Secreto!"
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img, mensaje, (50, 200), font, 3, (250, 255, 250), 10, cv2.LINE_AA)

# Añadir ruido en los canales rojo y verde
for i in range(height):
    for j in range(width):
        img[i, j, 1] += random.randint(0, 255)  # Canal verde
        img[i, j, 0] += random.randint(0, 255)  # Canal rojo

# Guardar la imagen
cv2.imwrite('mensajeOculto.png', img)


#desencriptado de imagen

Image("mensajeOculto.png")

imgMsgOculto = cv2.imread("mensajeOculto.png",cv2.IMREAD_COLOR)
plt.imshow(imgMsgOculto)

b,g,r = cv2.split(imgMsgOculto)
cv2.imwrite('mensajeNoOculto.png', r)

#Mostramos los canales por separado
plt.figure(figsize=[15,5])

plt.subplot(142)
plt.imshow(r, cmap="OrRd");plt.title("rojos")
plt.subplot(143)
plt.imshow(r, cmap="YlGn");plt.title("verdes")
plt.subplot(144)
plt.imshow(r, cmap="Blues");plt.title("azules")


#Combinamos los tres canales nuevamente

ImgCombinada = cv2.merge((b,g,r))
imgRGB = cv2.cvtColor(ImgCombinada, cv2.COLOR_BGR2RGB)


#Combinamos y mostramos

plt.subplot(141)
plt.imshow(imgRGB)
plt.tight_layout()
plt.title("canales combinados")
plt.show()








