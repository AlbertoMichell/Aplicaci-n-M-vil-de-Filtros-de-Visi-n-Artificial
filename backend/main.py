from fastapi import FastAPI, File, UploadFile, Form
from fastapi.responses import Response
import cv2
import numpy as np
from io import BytesIO
from typing import Optional

app = FastAPI(title="Image Processing API with OpenCV")

# leemos bytes y convertimos a imagen de OpenCV
def read_image_file(file: bytes) -> np.ndarray:
    nparr = np.frombuffer(file, np.uint8)
    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    return img

# convertimos imagen de OpenCV de vuelta a bytes JPEG
def encode_image(img: np.ndarray) -> bytes:
    success, encoded_image = cv2.imencode('.jpg', img)
    if not success:
        raise Exception("Error al codificar imagen")
    return encoded_image.tobytes()

# endpoint para verificar que el server responde
@app.get("/health")
async def health_check():
    return {"status": "ok", "message": "Servidor activo"}


# ajustamos brillo y contraste con formula lineal
@app.post("/filter/brightness_contrast")
async def brightness_contrast(
    file: UploadFile = File(...),
    brightness: int = Form(30),
    contrast: float = Form(1.3)
):
    contents = await file.read()
    img = read_image_file(contents)
    
    # alpha controla contraste, beta el brillo
    adjusted = cv2.convertScaleAbs(img, alpha=contrast, beta=brightness)
    
    return Response(content=encode_image(adjusted), media_type="image/jpeg")

# correccion gamma para ajustar luminosidad no lineal
@app.post("/filter/gamma")
async def gamma_correction(
    file: UploadFile = File(...),
    gamma: float = Form(1.5)
):
    contents = await file.read()
    img = read_image_file(contents)
    
    # armamos tabla de lookup con la curva gamma
    inv_gamma = 1.0 / gamma
    table = np.array([((i / 255.0) ** inv_gamma) * 255
                      for i in np.arange(0, 256)]).astype("uint8")
    
    corrected = cv2.LUT(img, table)
    
    return Response(content=encode_image(corrected), media_type="image/jpeg")

# invertimos los colores (negativo fotografico)
@app.post("/filter/negative")
async def negative(file: UploadFile = File(...)):
    contents = await file.read()
    img = read_image_file(contents)
    
    negative_img = 255 - img
    
    return Response(content=encode_image(negative_img), media_type="image/jpeg")

# reducimos niveles de color para efecto posterizado
@app.post("/filter/quantization")
async def quantization(
    file: UploadFile = File(...),
    levels: int = Form(4)
):
    contents = await file.read()
    img = read_image_file(contents)
    
    # limitamos el rango
    if levels < 2:
        levels = 2
    if levels > 256:
        levels = 256
    
    # cuantizamos por division entera
    step = 256 // levels
    quantized = (img // step) * step
    
    return Response(content=encode_image(quantized), media_type="image/jpeg")


# desenfoque gaussiano - suavizamos la imagen
@app.post("/filter/gaussian_blur")
async def gaussian_blur(
    file: UploadFile = File(...),
    kernel_size: int = Form(31)
):
    contents = await file.read()
    img = read_image_file(contents)
    
    # aseguramos kernel impar y minimo 3
    if kernel_size < 3:
        kernel_size = 3
    if kernel_size % 2 == 0:
        kernel_size += 1
    
    # sigma grande para blur notorio
    sigma = kernel_size / 2.0
    
    blurred = cv2.GaussianBlur(img, (kernel_size, kernel_size), sigma)
    
    return Response(content=encode_image(blurred), media_type="image/jpeg")

# filtro de mediana - bueno para quitar ruido salt & pepper
@app.post("/filter/median_blur")
async def median_blur(
    file: UploadFile = File(...),
    kernel_size: int = Form(9)
):
    contents = await file.read()
    img = read_image_file(contents)
    
    if kernel_size < 3:
        kernel_size = 3
    if kernel_size % 2 == 0:
        kernel_size += 1
    
    filtered = cv2.medianBlur(img, kernel_size)
    
    return Response(content=encode_image(filtered), media_type="image/jpeg")

# enfoque - acentuamos bordes con kernel custom
@app.post("/filter/sharpen")
async def sharpen(
    file: UploadFile = File(...),
    strength: float = Form(1.5)
):
    contents = await file.read()
    img = read_image_file(contents)
    
    # armamos kernel de enfoque dinamico
    center = 1 + 8 * strength
    edge = -strength
    kernel = np.array([[edge, edge, edge],
                       [edge, center, edge],
                       [edge, edge, edge]])
    
    sharpened = cv2.filter2D(img, -1, kernel)
    
    return Response(content=encode_image(sharpened), media_type="image/jpeg")

# sobel - detecta bordes con gradientes en x e y
@app.post("/filter/sobel")
async def sobel_edge_detection(file: UploadFile = File(...)):
    contents = await file.read()
    img = read_image_file(contents)
    
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    # calculamos gradientes
    sobelx = cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize=3)
    sobely = cv2.Sobel(gray, cv2.CV_64F, 0, 1, ksize=3)
    
    # magnitud total
    sobel = np.sqrt(sobelx**2 + sobely**2)
    sobel = np.uint8(sobel / sobel.max() * 255)
    
    sobel_bgr = cv2.cvtColor(sobel, cv2.COLOR_GRAY2BGR)
    
    return Response(content=encode_image(sobel_bgr), media_type="image/jpeg")

# laplaciano - segunda derivada para bordes
@app.post("/filter/laplacian")
async def laplacian_edge_detection(file: UploadFile = File(...)):
    contents = await file.read()
    img = read_image_file(contents)
    
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    laplacian = cv2.Laplacian(gray, cv2.CV_64F)
    laplacian = np.uint8(np.absolute(laplacian))
    
    laplacian_bgr = cv2.cvtColor(laplacian, cv2.COLOR_GRAY2BGR)
    
    return Response(content=encode_image(laplacian_bgr), media_type="image/jpeg")


# creamos kernel rectangular para morfologia
def get_morphological_kernel(size: int):
    return cv2.getStructuringElement(cv2.MORPH_RECT, (size, size))

# erosion - achica regiones blancas
@app.post("/filter/erosion")
async def erosion(
    file: UploadFile = File(...),
    kernel_size: int = Form(7)
):
    contents = await file.read()
    img = read_image_file(contents)
    
    # convertimos a binario primero
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    _, binary = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
    
    kernel = get_morphological_kernel(kernel_size)
    eroded = cv2.erode(binary, kernel, iterations=2)
    
    result = cv2.cvtColor(eroded, cv2.COLOR_GRAY2BGR)
    
    return Response(content=encode_image(result), media_type="image/jpeg")

# dilatacion - expande regiones blancas
@app.post("/filter/dilation")
async def dilation(
    file: UploadFile = File(...),
    kernel_size: int = Form(7)
):
    contents = await file.read()
    img = read_image_file(contents)
    
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    _, binary = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
    
    kernel = get_morphological_kernel(kernel_size)
    dilated = cv2.dilate(binary, kernel, iterations=2)
    
    result = cv2.cvtColor(dilated, cv2.COLOR_GRAY2BGR)
    
    return Response(content=encode_image(result), media_type="image/jpeg")

# apertura - erosion + dilatacion (quita ruido pequeño)
@app.post("/filter/opening")
async def opening(
    file: UploadFile = File(...),
    kernel_size: int = Form(7)
):
    contents = await file.read()
    img = read_image_file(contents)
    
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    _, binary = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
    
    kernel = get_morphological_kernel(kernel_size)
    opened = cv2.morphologyEx(binary, cv2.MORPH_OPEN, kernel, iterations=2)
    
    result = cv2.cvtColor(opened, cv2.COLOR_GRAY2BGR)
    
    return Response(content=encode_image(result), media_type="image/jpeg")

# cierre - dilatacion + erosion (rellena huecos)
@app.post("/filter/closing")
async def closing(
    file: UploadFile = File(...),
    kernel_size: int = Form(7)
):
    contents = await file.read()
    img = read_image_file(contents)
    
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    _, binary = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
    
    kernel = get_morphological_kernel(kernel_size)
    closed = cv2.morphologyEx(binary, cv2.MORPH_CLOSE, kernel, iterations=2)
    
    result = cv2.cvtColor(closed, cv2.COLOR_GRAY2BGR)
    
    return Response(content=encode_image(result), media_type="image/jpeg")


# canny - detector de bordes mas sofisticado con dos umbrales
@app.post("/filter/canny")
async def canny_edge_detection(
    file: UploadFile = File(...),
    threshold1: int = Form(50),
    threshold2: int = Form(150)
):
    contents = await file.read()
    img = read_image_file(contents)
    
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(gray, threshold1, threshold2)
    result = cv2.cvtColor(edges, cv2.COLOR_GRAY2BGR)
    
    return Response(content=encode_image(result), media_type="image/jpeg")

# convertimos a escala de grises simple
@app.post("/filter/grayscale")
async def grayscale(file: UploadFile = File(...)):
    contents = await file.read()
    img = read_image_file(contents)
    
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    result = cv2.cvtColor(gray, cv2.COLOR_GRAY2BGR)
    
    return Response(content=encode_image(result), media_type="image/jpeg")

# encontramos y dibujamos contornos
@app.post("/filter/contours")
async def contour_detection(file: UploadFile = File(...)):
    contents = await file.read()
    img = read_image_file(contents)
    
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    _, binary = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
    
    # detectamos contornos externos
    contours, _ = cv2.findContours(binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    # dibujamos en verde sobre la imagen original
    result = img.copy()
    cv2.drawContours(result, contours, -1, (0, 255, 0), 2)
    
    return Response(content=encode_image(result), media_type="image/jpeg")

# ecualizacion de histograma para mejorar contraste
@app.post("/filter/histogram_equalization")
async def histogram_equalization(file: UploadFile = File(...)):
    contents = await file.read()
    img = read_image_file(contents)
    
    # trabajamos en espacio YCrCb para ecualizar solo luminancia
    ycrcb = cv2.cvtColor(img, cv2.COLOR_BGR2YCrCb)
    ycrcb[:, :, 0] = cv2.equalizeHist(ycrcb[:, :, 0])
    result = cv2.cvtColor(ycrcb, cv2.COLOR_YCrCb2BGR)
    
    return Response(content=encode_image(result), media_type="image/jpeg")

# arrancamos el server
if __name__ == "__main__":
    import uvicorn
    import os
    port = int(os.environ.get("PORT", 8001))
    uvicorn.run(app, host="0.0.0.0", port=port)
