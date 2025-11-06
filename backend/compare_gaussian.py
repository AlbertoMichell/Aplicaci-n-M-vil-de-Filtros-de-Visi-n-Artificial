import cv2
import numpy as np

files = ['gaussian_input.jpg','gaussian_k3.jpg','gaussian_k5.jpg','gaussian_k11.jpg','gaussian_k25.jpg']
input_img = cv2.imread(files[0])

print('Comparando con input (medias absolutas por canal y MSE total):')
for f in files[1:]:
    img = cv2.imread(f)
    if img is None:
        print(f, 'NO CARGADA')
        continue
    # asegurar mismo tamaño
    if img.shape != input_img.shape:
        print(f, 'tamaño diferente')
        continue
    diff = cv2.absdiff(input_img, img)
    mad_per_channel = diff.mean(axis=(0,1))
    mse = (diff.astype('float32')**2).mean()
    print(f, 'MAD BGR=', mad_per_channel, 'MSE=', mse)
