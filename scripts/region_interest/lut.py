import cv2
import numpy as np

# Carga las dos imágenes
imagen1 = cv2.imread('D:/dataset/HAM10000_images_part_1/ISIC_0024307.jpg')
imagen2 = cv2.imread('D:/dataset/HAM10000_images_part_1/ISIC_0024307.jpg')

# Convierte las imágenes a escala de grises
imagen1_gris = cv2.cvtColor(imagen1, cv2.COLOR_BGR2GRAY)
imagen2_gris = cv2.cvtColor(imagen2, cv2.COLOR_BGR2GRAY)

# Calcula los histogramas de ambas imágenes
hist1, bins1 = np.histogram(imagen1_gris.ravel(), 256, [0, 256])
hist2, bins2 = np.histogram(imagen2_gris.ravel(), 256, [0, 256])

# Normaliza los histogramas
hist1_norm = hist1.cumsum() / hist1.sum()
hist2_norm = hist2.cumsum() / hist2.sum()

# Calcula la correspondencia de histogramas
tabla_correspondencia = np.interp(hist1_norm, hist2_norm, bins2)

# Aplica la tabla de correspondencia a la imagen1
imagen1_ajustada = cv2.LUT(imagen1_gris, tabla_correspondencia)

# Convierte la imagen ajustada de vuelta a color
imagen1_ajustada = cv2.cvtColor(imagen1_ajustada, cv2.COLOR_GRAY2BGR)

# Muestra la imagen ajustada
cv2.imshow('Imagen ajustada', imagen1_ajustada)
cv2.waitKey(0)
cv2.destroyAllWindows()