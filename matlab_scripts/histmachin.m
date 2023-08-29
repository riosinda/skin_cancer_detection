% Cargar las imágenes de origen y destino
imagen_origen = imread('D:/SkinCancerDatasets/HAM10000/HAM10000_images/ISIC_0024312.jpg');
imagen_destino = imread('D:/SkinCancerDatasets/HAM10000/HAM10000_images/ISIC_0024306.jpg');

% Realizar la coincidencia de histograma
imagen_coincidente = imhistmatch(imagen_origen, imagen_destino);

% Mostrar las imágenes originales y la imagen con histograma coincidente
subplot(1, 3, 1), imshow(imagen_origen), title('bad_image');
subplot(1, 3, 2), imshow(imagen_destino), title('base');
subplot(1, 3, 3), imshow(imagen_coincidente), title('HistoCoincident');
