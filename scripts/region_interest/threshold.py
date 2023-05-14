import numpy as np
import cv2
import matplotlib.pyplot as plt

cont = 7
while True:
    if cont < 10:
        img = cv2.imread('D:/dataset/HAM10000_images_part_1/ISIC_002430'+str(cont)+'.jpg')
    else:
        img = cv2.imread('D:/dataset/HAM10000_images_part_1/ISIC_00243'+str(cont)+'.jpg')
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    imagen = img.copy()
    gray = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)
    blur = cv2.medianBlur(gray,5)   #filtro para reduccion de ruido

    _,thresh = cv2.threshold(blur,np.max(blur)-45,255,cv2.THRESH_BINARY_INV)    #umbral de binarizacion

    for i in range(0,thresh.shape[0]):
        for j in range(0,thresh.shape[1]):
            if thresh[i,j] != 255:
                imagen[i,j] = 0

    fig, axs = plt.subplots(1, 3)

    # Graficar las imágenes en cada subtrama
    axs[0].imshow(img,)
    axs[0].set_title('original')
    axs[1].imshow(thresh, cmap='gray')
    axs[1].set_title('threshold')
    axs[2].imshow(imagen,)
    axs[2].set_title('interest_area')

    # Mostrar la figura durante 1 segundo
    plt.pause(3)

    # Cerrar la figura
    plt.close(fig)
    cont=cont+1


#contornos activo
#otsu
#agrupamientos
#armonicos de fourier


#machine de histogramas
#reggion props #deteccion por areas


