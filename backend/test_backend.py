import requests
import os

BASE_URL = "http://localhost:8000"

def test_health_check():
    print("\n1. Probando conexión...")
    response = requests.get(f"{BASE_URL}/health")
    assert response.status_code == 200
    print("   OK - Servidor respondiendo correctamente")

def test_filter_endpoint():
    print("\n2. Probando filtro de negativo...")
    
    test_image_path = "test_image.jpg"
    
    if not os.path.exists(test_image_path):
        print("   ADVERTENCIA: No se encontro test_image.jpg")
        print("   Por favor agrega una imagen de prueba llamada test_image.jpg")
        return
    
    with open(test_image_path, 'rb') as f:
        files = {'file': f}
        response = requests.post(f"{BASE_URL}/filter/negative", files=files)
    
    if response.status_code == 200:
        print("   OK - Filtro aplicado correctamente")
        with open("test_result.jpg", 'wb') as f:
            f.write(response.content)
        print("   Resultado guardado en test_result.jpg")
    else:
        print(f"   ERROR: {response.status_code}")
        print(f"   {response.text}")

def test_filter_with_parameters():
    print("\n3. Probando filtro con parametros (brillo y contraste)...")
    
    test_image_path = "test_image.jpg"
    
    if not os.path.exists(test_image_path):
        print("   ADVERTENCIA: No se encontro test_image.jpg")
        return
    
    with open(test_image_path, 'rb') as f:
        files = {'file': f}
        data = {'brightness': 50, 'contrast': 1.5}
        response = requests.post(
            f"{BASE_URL}/filter/brightness_contrast",
            files=files,
            data=data
        )
    
    if response.status_code == 200:
        print("   OK - Filtro con parametros aplicado correctamente")
        with open("test_brightness.jpg", 'wb') as f:
            f.write(response.content)
        print("   Resultado guardado en test_brightness.jpg")
    else:
        print(f"   ERROR: {response.status_code}")

if __name__ == "__main__":
    print("=" * 60)
    print("PRUEBAS DEL BACKEND - API de Procesamiento de Imagenes")
    print("=" * 60)
    
    try:
        test_health_check()
        test_filter_endpoint()
        test_filter_with_parameters()
        
        print("\n" + "=" * 60)
        print("PRUEBAS COMPLETADAS EXITOSAMENTE")
        print("=" * 60)
        
    except requests.exceptions.ConnectionError:
        print("\nERROR: No se pudo conectar al servidor")
        print("Asegurate de que el backend este corriendo en http://localhost:8000")
        print("Ejecuta: python main.py")
        
    except Exception as e:
        print(f"\nERROR: {e}")
