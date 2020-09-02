import os
import shutil
import sys

# Caminho arquivo original Wider Face
origin ='D:/TCS/Health Tech/TensorFlow/workspace/training_demo/annotations/wider face pascal voc annotations/WIDER_val_annotations/'
# Caminho pasta de imagens (train, val, test)
# destination ='D:/TCS/Health Tech/TensorFlow/workspace/training_demo/images/val/'
destination ='D:/TCS/dummy/'


# Nome dos arquivos
file_names = os.listdir(origin)
# Nome das pastas
folder_names = os.listdir(destination)

# Arquivos com inicio igual ou maior que 10
for iter_classes in range(0, 60):
    for iter_files in range(len(file_names)):
        if file_names[iter_files][:2] == folder_names[iter_classes][:2]:
            shutil.copy(origin+file_names[iter_files], destination+folder_names[iter_classes])

# Arquivos com inicio menor que 10
for iter_classes in range(0, 60):
    for iter_files in range(len(file_names)):
        if folder_names[iter_classes][1:2] == '-':
            if file_names[iter_files][1:2] == '_':
                if file_names[iter_files][:1] == folder_names[iter_classes][:1]:
                    shutil.copy(origin+file_names[iter_files], destination+folder_names[iter_classes])