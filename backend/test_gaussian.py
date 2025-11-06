import requests
import numpy as np
import cv2

BASE_URL = "https://filtros-vision-mich-production.up.railway.app"

w, h = 800, 600
gradient = np.linspace(0, 255, w, dtype=np.uint8)
img = np.tile(gradient, (h, 1))
img_color = cv2.merge([img, img, img])

cv2.imwrite('gaussian_input.jpg', img_color)

kernel_sizes = [3, 5, 11, 25]
for k in kernel_sizes:
    files = {'file': ('gaussian_input.jpg', open('gaussian_input.jpg', 'rb'), 'image/jpeg')}
    data = {'kernel_size': str(k)}
    print(f"Enviando kernel_size={k}...")
    r = requests.post(f"{BASE_URL}/filter/gaussian_blur", files=files, data=data, timeout=30)
    if r.status_code == 200:
        out_name = f'gaussian_k{k}.jpg'
        with open(out_name, 'wb') as f:
            f.write(r.content)
        print(f"  OK -> {out_name} guardado")
    else:
        print(f"  ERROR {r.status_code}: {r.text}")

print("Prueba completada")
