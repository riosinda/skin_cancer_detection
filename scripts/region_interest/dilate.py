import cv2
import numpy as np

# Cargar imagen binaria con huecos
img = cv2.imread('mask.png')

# Definir tamaño del elemento estructural
kernel = np.ones((3,3), np.uint8)

# Dilatar píxeles negros para rellenar huecos
img_dilation = cv2.dilate(img, kernel, iterations=3)

# Mostrar imagen original y la imagen con huecos rellenos
cv2.imshow('Imagen Original', img)
cv2.imshow('Imagen con Huecos Rellenos', img_dilation)
cv2.waitKey(0)
cv2.destroyAllWindows()