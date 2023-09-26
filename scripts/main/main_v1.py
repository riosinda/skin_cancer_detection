import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.applications import InceptionV3
from tensorflow.keras.layers import Dense, GlobalAveragePooling2D
from tensorflow.keras.models import Model

import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix, classification_report
from sklearn.utils.multiclass import unique_labels

train_dir = 'D:/SkinCancerDatasets/FinalDataset/train/'
test_dir = 'D:/SkinCancerDatasets/FinalDataset/test/'

num_classes = 2  # Dos clases en tu dataset (por ejemplo, 'gato' y 'perro')
batch_size = 32
epochs = 60

train_datagen = ImageDataGenerator(
    rescale=1.0 / 255,
    shear_range=0.2,
    zoom_range=0.2,
    horizontal_flip=True,
)

test_datagen = ImageDataGenerator(rescale=1.0 / 255)

train_generator = train_datagen.flow_from_directory(
    train_dir,
    target_size=(224, 224),  # Tamaño de entrada de InceptionV3
    batch_size=batch_size,
    class_mode='binary',  # Modo binario para dos clases
)

test_generator = test_datagen.flow_from_directory(
    test_dir,
    target_size=(224, 224),
    batch_size=batch_size,
    class_mode='binary',
)

base_model = InceptionV3(weights='imagenet', include_top=False)

x = base_model.output
x = GlobalAveragePooling2D()(x)
x = Dense(1024, activation='relu')(x)
predictions = Dense(1, activation='sigmoid')(x)  # Una neurona para clasificación binaria

model = Model(inputs=base_model.input, outputs=predictions)

for layer in base_model.layers:
    layer.trainable = False

model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

history = model.fit(
    train_generator,
    steps_per_epoch=len(train_generator),
    epochs=epochs,
    validation_data=test_generator,
    validation_steps=len(test_generator),
)

test_loss, test_accuracy = model.evaluate(test_generator, steps=len(test_generator))
print(f'Loss: {test_loss}, Accuracy: {test_accuracy}')


y_pred = model.predict(test_generator, steps=len(test_generator)).round()

y_true = test_generator.classes

confusion = confusion_matrix(y_true, y_pred)

class_names = unique_labels(y_true, y_pred)


plt.figure(figsize=(8, 6))
sns.set(font_scale=1.2)
sns.heatmap(confusion, annot=True, fmt='d', cmap='Blues', cbar=False,
            xticklabels=class_names, yticklabels=class_names)
plt.xlabel('Predicted')
plt.ylabel('True')
plt.title('Matriz de Confusión')
plt.show()


report = classification_report(y_true, y_pred)
print("\nInforme de Clasificación:")
print(report)