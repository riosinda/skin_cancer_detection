import os
import csv

# Ruta de la carpeta donde se encuentran los archivos
carpeta = "D:/dataset/HAM10000_images_part_2"

# Obtener una lista de los nombres de los archivos en la carpeta
nombres_archivos = os.listdir(carpeta)

# Crear un archivo CSV y escribir los nombres de los archivos en él
with open("HAM10000_images_part_2.csv", "w", newline="") as archivo_csv:
    escritor_csv = csv.writer(archivo_csv)
    escritor_csv.writerow(["names_files"])
    for nombre_archivo in nombres_archivos:
        escritor_csv.writerow([nombre_archivo])
        print(nombre_archivo)


