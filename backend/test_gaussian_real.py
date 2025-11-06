import requests
import numpy as np
import cv2
import sys

BASE_URL = "https://filtros-vision-mich-production.up.railway.app"

img = np.ones((400, 600, 3), dtype=np.uint8) * 255
cv2.putText(img, 'BLUR TEST', (50, 200), cv2.FONT_HERSHEY_SIMPLEX, 3, (0, 0, 0), 5)
cv2.imwrite('blur_test_input.jpg', img)

print("Enviando imagen al endpoint de desenfoque gaussiano...")
print(f"URL: {BASE_URL}/filter/gaussian_blur")

files = {'file': ('blur_test_input.jpg', open('blur_test_input.jpg', 'rb'), 'image/jpeg')}

try:
    r = requests.post(f"{BASE_URL}/filter/gaussian_blur", files=files, timeout=30)
    print(f"Status code: {r.status_code}")
    
    if r.status_code == 200:
        with open('blur_test_output.jpg', 'wb') as f:
            f.write(r.content)
        print("✓ Imagen procesada guardada en blur_test_output.jpg")
        
        output = cv2.imread('blur_test_output.jpg')
        diff = cv2.absdiff(img, output)
        mean_diff = diff.mean()
        print(f"Diferencia media entre input y output: {mean_diff:.2f}")
        
        if mean_diff > 10:
            print("✓ El filtro está aplicando cambios significativos")
        else:
            print("⚠ El filtro tiene efecto mínimo")
    else:
        print(f"✗ Error: {r.text}")
        sys.exit(1)
        
except Exception as e:
    print(f"✗ Error: {e}")
    sys.exit(1)
