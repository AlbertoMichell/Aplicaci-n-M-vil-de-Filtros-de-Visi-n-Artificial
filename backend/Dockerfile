# Dockerfile para el Backend
FROM python:3.9-slim

WORKDIR /app

# Instalar dependencias del sistema necesarias para OpenCV
RUN apt-get update && apt-get install -y \
    libglib2.0-0 \
    libsm6 \
    libxext6 \
    libxrender-dev \
    libgomp1 \
    libgl1-mesa-glx \
    && rm -rf /var/lib/apt/lists/*

# Copiar requirements
COPY requirements.txt .

# Instalar dependencias Python
RUN pip install --no-cache-dir -r requirements.txt

# Copiar codigo
COPY main.py .

# Exponer puerto (Railway asigna dinámicamente)
EXPOSE 8000

# Comando para ejecutar (usa variable PORT de Railway)
CMD python main.py
