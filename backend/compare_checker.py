import cv2
import numpy as np

files = ['checker_input.jpg','checker_k3.jpg','checker_k5.jpg','checker_k11.jpg','checker_k25.jpg']
input_img = cv2.imread(files[0])
print('MAD and MSE for checker tests:')
for f in files[1:]:
    img = cv2.imread(f)
    diff = cv2.absdiff(input_img,img)
    mad = diff.mean()
    mse = (diff.astype('float32')**2).mean()
    print(f, 'MAD=', mad, 'MSE=', mse)
